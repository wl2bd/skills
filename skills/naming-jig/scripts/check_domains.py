#!/usr/bin/env python3
"""Check domain availability for name candidates via RDAP.

RDAP is the structured successor to WHOIS. This script resolves each TLD to
its authoritative registry through the IANA bootstrap registry, then queries
that registry directly.

It deliberately does NOT go through a public redirector. A redirector answers
404 for every TLD it does not serve, and that is indistinguishable from "no
registration found" -- the one error that makes a naming process hand over a
name somebody else already owns.

Interpretation of results:
  REGISTERED  -> the registry returned a domain object (taken)
  AVAILABLE?  -> the authoritative registry answered 404 (no registration
                 found). Likely available. ALWAYS confirm at a registrar
                 before treating the domain as yours.
  NO RDAP     -> nothing could be checked for this TLD. NOT a verdict about
                 the domain. Check it at a registrar by hand.
  UNKNOWN     -> the registry was unreachable, rate-limited, or answered
                 something unusable. Check manually.

Before checking candidates on a TLD, the script runs one control lookup on
nic.<tld>, which every registry operates. If that control does not come back
REGISTERED, the registry is not answering reliably, and every candidate on
that TLD is reported UNKNOWN instead of AVAILABLE?. Without this control, a
registry that 404s everything reads as a shortlist of free domains.

Roughly 180 TLDs publish no RDAP service at all (.io, .de, .eu, .co, .ch,
.it, .es, .ru among them). For those the script falls back to WHOIS, whose
answers are free text in no agreed format. Rather than parse them, it asks
each registry two questions whose answers are already known -- nic.<tld> is
always taken, a long random label never is -- and classifies candidates by
which of the two replies they resemble. A candidate that resembles both
about equally is reported UNKNOWN. If the registry does not visibly tell the
two controls apart, the whole TLD stays NO RDAP. Results obtained this way
are flagged in the output: the signal is WHOIS, not RDAP.

Usage:
  python3 check_domains.py lumafold amberpost --tlds com,ai,app
  python3 check_domains.py "two words" --tlds com   (spaces are stripped)
  python3 check_domains.py écrin cœur --tlds fr     (accents are transliterated,
                                                     and the rewrite is printed)

Stdlib only. Be polite: the script sleeps between queries; don't hammer
registries with hundred-name lists; verify shortlists, not raw sheets.
"""

import argparse
import difflib
import json
import re
import socket
import sys
import time
import unicodedata
import urllib.error
import urllib.request

IANA_BOOTSTRAP = "https://data.iana.org/rdap/dns.json"
DEFAULT_TLDS = ["com", "ai", "app", "io", "dev", "tools"]
DELAY_SECONDS = 0.6
TIMEOUT_SECONDS = 15
RETRIES = 2
CONTROL_LABEL = "nic"

WHOIS_IANA = "whois.iana.org"
WHOIS_PORT = 43
WHOIS_TIMEOUT = 15
PROBE_LABEL = "zz-naming-jig-probe-9731"
# How far apart the two similarity scores must be before a WHOIS answer is
# called either way. Below this, the answer resembles both controls about
# equally, which is not evidence of anything.
MARGIN = 0.15
# How much an answer must actually look like the "no such domain" control
# before it is called free. A relative win is not enough: the free control is
# a short sentence and difflib's ratio is 2*M/(len(a)+len(b)), so ANY short
# reply outscores the long "registered" control by construction -- including
# every rate-limit notice a registry sends once you query it in bulk.
FREE_FLOOR = 0.6
# A registry that is throttling, refusing or down says so in prose, and
# reading a refusal as an absence is what turns a busy registry into a list
# of free domains. Careful: registries also describe their throttling policy
# inside the terms of use attached to every answer, so these words only mean
# a refusal when the answer is short enough to be nothing else.
REFUSAL_MARKERS = (
    "exceeded", "too many", "rate limit", "quota", "access denied",
    "connection refused", "try again", "temporarily unavailable",
    "not permitted", "unauthorized", "forbidden", "blocked",
)
REFUSAL_MAX_CHARS = 400

# Latin letters with no Unicode decomposition: NFKD leaves them untouched,
# so they need an explicit ASCII spelling or they would be dropped.
TRANSLITERATE = {
    "æ": "ae", "œ": "oe", "ø": "o", "ß": "ss", "þ": "th",
    "ð": "d", "đ": "d", "ł": "l", "ħ": "h", "ı": "i",
}


def normalize(name: str) -> str:
    """Lowercase and transliterate a candidate to a valid ASCII domain label.

    Transliterates rather than deletes. Deleting would turn "écrin" into
    "crin" and silently check the wrong domain.
    """
    name = name.strip().lower().replace(" ", "")
    name = "".join(TRANSLITERATE.get(c, c) for c in name)
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    name = re.sub(r"[^a-z0-9-]", "", name)
    return name.strip("-")


LAST_ERROR = [None]


def fetch(url: str):
    """GET a URL, return (http_status_or_None, parsed_body_or_None).

    Retries on throttling, server errors and timeouts. Registries throttle
    aggressively, and a 429 must never be allowed to look like an answer
    about the domain itself. The last transport error is kept in LAST_ERROR
    so callers can tell a broken local setup from a registry outage.
    """
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/rdap+json",
            "User-Agent": "naming-jig-domain-check/2.0",
        },
    )
    delay = 1.0
    for attempt in range(RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                try:
                    return resp.status, json.load(resp)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    return resp.status, None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, None
            if e.code in (429, 500, 502, 503, 504) and attempt < RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            return e.code, None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            LAST_ERROR[0] = "{}: {}".format(type(e).__name__, e)
            if attempt < RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            return None, None
    return None, None


def load_registry():
    """Map each TLD to its authoritative RDAP base URL, per IANA.

    Returns None if the bootstrap registry itself cannot be read: without it
    a 404 cannot be told apart from an unserved TLD, so no verdict is safe.
    """
    status, data = fetch(IANA_BOOTSTRAP)
    if status != 200 or not data:
        return None
    registry = {}
    for entry in data.get("services", []):
        if len(entry) < 2:
            continue
        tlds, urls = entry[0], entry[1]
        base = next((u for u in urls if u.startswith("https://")), None)
        if not base:
            continue
        for tld in tlds:
            registry[tld.lower()] = base.rstrip("/")
    return registry or None


def whois_query(server: str, query: str):
    """Send one WHOIS query on port 43, return the raw text or None.

    Retries on connection failures and on an explicit refusal: WHOIS
    servers throttle hard, and a refusal that slips through would be read
    as an answer about the domain.
    """
    delay = 2.0
    for attempt in range(RETRIES + 1):
        try:
            with socket.create_connection((server, WHOIS_PORT),
                                          timeout=WHOIS_TIMEOUT) as sock:
                sock.settimeout(WHOIS_TIMEOUT)
                sock.sendall((query + "\r\n").encode("utf-8", "replace"))
                chunks, total = [], 0
                while total < 200000:
                    data = sock.recv(4096)
                    if not data:
                        break
                    chunks.append(data)
                    total += len(data)
            body = b"".join(chunks).decode("utf-8", "replace")
            if body and looks_refused(body) and attempt < RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            return body
        except OSError:
            if attempt < RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            return None
    return None


def whois_server_for(tld: str):
    """Ask IANA which WHOIS server is authoritative for a TLD."""
    body = whois_query(WHOIS_IANA, tld)
    if not body:
        return None
    for line in body.splitlines():
        if line.lower().startswith("whois:"):
            server = line.split(":", 1)[1].strip()
            if server:
                return server
    return None


def has_refusal_marker(text: str) -> bool:
    low = text.lower()
    return any(marker in low for marker in REFUSAL_MARKERS)


def looks_refused(text: str) -> bool:
    """True when the whole answer is a refusal rather than a record.

    Length-gated on purpose: every registry ships its throttling policy in
    the terms of use attached to normal answers, so matching those words in
    a full record would reject the registries that document themselves best.
    """
    return len(text) <= REFUSAL_MAX_CHARS and has_refusal_marker(text)


def whois_lines(text: str, domain: str):
    """Normalize a WHOIS answer into comparable lines.

    Strips the queried domain, digits and comment markers, so that two
    answers differ only where the registry actually said something different.
    """
    out = []
    for line in text.lower().splitlines():
        line = line.replace(domain.lower(), "")
        line = re.sub(r"[0-9]+", "", line)
        line = re.sub(r"\s+", " ", line).strip(" \t.")
        if line and not line.startswith(("%", "#", ">>>")):
            out.append(line)
    return out


def discriminating(lines, boilerplate) -> str:
    """Keep only what is not in both control answers."""
    return " ".join(line for line in lines if line not in boilerplate)


def whois_controls(tld: str):
    """Learn what "taken" and "free" look like on this registry.

    WHOIS answers are free text in no agreed format, so instead of parsing
    them we ask two questions whose answers are already known -- nic.<tld> is
    always taken, a long random label never is. Everything the two answers
    share is legal boilerplate and gets subtracted; what survives is the part
    that actually carries the verdict. Returns None when the registry does
    not visibly distinguish the two, which must stay a non-answer rather than
    become a guess.
    """
    server = whois_server_for(tld)
    if not server:
        return None
    taken_domain = "{}.{}".format(CONTROL_LABEL, tld)
    free_domain = "{}.{}".format(PROBE_LABEL, tld)
    taken = whois_query(server, taken_domain)
    time.sleep(DELAY_SECONDS)
    free = whois_query(server, free_domain)
    time.sleep(DELAY_SECONDS)
    if not taken or not free:
        return None
    # Controls learned from a throttled server describe the throttling, not
    # the registry, and every candidate would then be measured against noise.
    if looks_refused(taken) or looks_refused(free):
        return None

    taken_lines, free_lines = whois_lines(taken, taken_domain), whois_lines(free, free_domain)
    boilerplate = set(taken_lines) & set(free_lines)
    taken_fp = discriminating(taken_lines, boilerplate)
    free_fp = discriminating(free_lines, boilerplate)
    # Nothing left once the shared text is gone: the registry answered the
    # same thing both times (an access-denied notice, usually).
    if not taken_fp or not free_fp:
        return None
    if difflib.SequenceMatcher(None, taken_fp, free_fp).ratio() > 0.85:
        return None
    return (server, boilerplate, set(free_lines) - boilerplate,
            set(taken_lines) - boilerplate, free_fp, taken_fp)


def check_whois(controls, domain: str) -> str:
    server, boilerplate, free_markers, taken_markers, free_fp, taken_fp = controls
    body = whois_query(server, domain)
    if not body or looks_refused(body):
        return "UNKNOWN"
    lines = whois_lines(body, domain)
    seen = set(lines)

    # "Domain not found", "Status: free", "Status: AVAILABLE" -- a registry
    # phrases its no-such-domain answer the same way every time, so an exact
    # line match is a stronger signal than any similarity score.
    hit_free, hit_taken = bool(free_markers & seen), bool(taken_markers & seen)
    if hit_free and not hit_taken:
        return "AVAILABLE?"
    if hit_taken and not hit_free:
        return "REGISTERED"

    fp = discriminating(lines, boilerplate)
    if not fp:
        return "UNKNOWN"
    # The terms of use are gone by now, being common to both controls, so a
    # refusal word surviving here was addressed to this query.
    if has_refusal_marker(fp):
        return "UNKNOWN"
    to_free = difflib.SequenceMatcher(None, fp, free_fp).ratio()
    to_taken = difflib.SequenceMatcher(None, fp, taken_fp).ratio()
    if abs(to_free - to_taken) < MARGIN:
        return "UNKNOWN"
    if to_free <= to_taken:
        return "REGISTERED"
    # Beating the long "registered" control is free for any short string, so
    # calling a domain available needs positive proof, not a relative win.
    return "AVAILABLE?" if to_free >= FREE_FLOOR else "UNKNOWN"


def check(base: str, domain: str) -> str:
    status, data = fetch("{}/domain/{}".format(base, domain))
    if status == 404:
        return "AVAILABLE?"
    if status == 200:
        if data and (data.get("objectClassName") == "domain" or data.get("ldhName")):
            return "REGISTERED"
        # A 200 carrying no RDAP object is a proxy, a captive portal or a
        # throttling page. It is not evidence that the domain exists.
        return "UNKNOWN"
    return "UNKNOWN"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="RDAP availability check for name candidates."
    )
    parser.add_argument("names", nargs="+", help="Name candidates (without TLD).")
    parser.add_argument(
        "--tlds",
        default=",".join(DEFAULT_TLDS),
        help="Comma-separated TLD list (default: %(default)s).",
    )
    parser.add_argument(
        "--no-control",
        action="store_true",
        help="Skip the nic.<tld> control lookup. Saves one request per TLD and "
             "loses the guard against a registry that answers 404 for everything.",
    )
    parser.add_argument(
        "--no-whois",
        action="store_true",
        help="Do not fall back to WHOIS for TLDs with no RDAP service; report "
             "them as NO RDAP instead.",
    )
    args = parser.parse_args()

    tlds = [t.strip().lstrip(".").lower() for t in args.tlds.split(",") if t.strip()]
    # Two candidates can normalize to the same label ("Sun Ray" and "SunRay"),
    # and some leave nothing at all ("北斗"). Both must be visible: a table
    # with a missing row reads as if everything was checked.
    names, rewritten, dropped, spellings = [], [], [], {}
    for raw in args.names:
        raw = raw.strip()
        name = normalize(raw)
        if not name:
            dropped.append(raw)
            continue
        if name != raw.lower().replace(" ", ""):
            rewritten.append((raw, name))
        if name in spellings:
            spellings[name].append(raw)
            continue
        spellings[name] = [raw]
        names.append(name)
    if not names or not tlds:
        print("Nothing to check after normalization.", file=sys.stderr)
        return 1

    registry = load_registry()
    if registry is None:
        print("Could not read the IANA RDAP bootstrap registry:", file=sys.stderr)
        print("  {}".format(IANA_BOOTSTRAP), file=sys.stderr)
        if LAST_ERROR[0]:
            print("  {}".format(LAST_ERROR[0]), file=sys.stderr)
            print("On macOS, CERTIFICATE_VERIFY_FAILED usually means a", file=sys.stderr)
            print("python.org install without its 'Install Certificates.command'.", file=sys.stderr)
            print("Behind a corporate proxy, set HTTPS_PROXY.", file=sys.stderr)
        print("Without this registry, a 404 cannot be told apart from a TLD", file=sys.stderr)
        print("that has no RDAP service, so no verdict here would be safe.", file=sys.stderr)
        print("Check these by hand at a registrar instead:", file=sys.stderr)
        for name in names:
            for tld in tlds:
                print("  {}.{}".format(name, tld), file=sys.stderr)
        return 1

    for raw, name in rewritten:
        print('note: "{}" is checked as "{}", its ASCII form.'.format(raw, name))
    if rewritten:
        print("      The accented spelling is a separate IDN registration;")
        print("      check it at a registrar if the brand will use it.")
        print()
    for name, raws in spellings.items():
        if len(raws) > 1:
            print('note: {} all normalize to "{}" and are checked once.'.format(
                ", ".join('"{}"'.format(r) for r in raws), name))
    if any(len(r) > 1 for r in spellings.values()):
        print()
    for raw in dropped:
        print('note: "{}" leaves no ASCII label, so it was NOT checked.'.format(raw))
    if dropped:
        print("      Look it up as an internationalized domain at a registrar.")
        print()

    # Resolve each TLD once, and prove the registry discriminates before
    # trusting a single answer from it.
    plan, forced, unserved, unreliable, via_whois = {}, {}, [], [], []
    for tld in tlds:
        base = registry.get(tld)
        if base is not None:
            plan[tld] = ("rdap", base)
            if args.no_control:
                continue
            control = check(base, "{}.{}".format(CONTROL_LABEL, tld))
            time.sleep(DELAY_SECONDS)
            if control != "REGISTERED":
                forced[tld] = "UNKNOWN"
                unreliable.append(tld)
            continue
        # No RDAP service. WHOIS still answers for most of these TLDs, but
        # only counts once the registry has proven it distinguishes a taken
        # domain from a free one.
        controls = None if args.no_whois else whois_controls(tld)
        if controls is None:
            forced[tld] = "NO RDAP"
            unserved.append(tld)
        else:
            plan[tld] = ("whois", controls)
            via_whois.append(tld)

    if via_whois:
        print("No RDAP service for: {}. Checked over WHOIS instead, against a".format(
            ", ".join("." + t for t in via_whois)))
        print("known-taken and a known-free control on each registry. Say so when")
        print("you report these: the signal is WHOIS, not RDAP.")
        print()
    if unserved:
        print("Not checkable: {}. No RDAP service, and WHOIS did not answer or".format(
            ", ".join("." + t for t in unserved)))
        print("did not distinguish taken from free. Those columns are not a verdict —")
        print("nothing was checked there. Look them up at a registrar by hand.")
        print()
    if unreliable:
        print("Control lookup failed for: {}. That registry is not answering".format(
            ", ".join("." + t for t in unreliable)))
        print("reliably, so its results are reported UNKNOWN, never AVAILABLE?.")
        print()

    col = max(len(n) for n in names) + 2
    header = "name".ljust(col) + "".join(("." + t).ljust(14) for t in tlds)
    print(header)
    print("-" * len(header))

    seen = set()
    for name in names:
        row = name.ljust(col)
        for tld in tlds:
            if tld in forced:
                status = forced[tld]
            else:
                kind, handle = plan[tld]
                domain = "{}.{}".format(name, tld)
                status = (check(handle, domain) if kind == "rdap"
                          else check_whois(handle, domain))
                time.sleep(DELAY_SECONDS)
            seen.add(status)
            row += status.ljust(14)
        print(row)

    print()
    if "AVAILABLE?" in seen:
        print("REGISTERED = taken at the registry. It may still be parked and for")
        print("             sale; the price, not the status, decides if it matters.")
        print("AVAILABLE? = no registration found at the authoritative registry.")
        print("             Confirm at a registrar before committing to the name")
        print("             or mentioning it publicly.")
    if "NO RDAP" in seen:
        print("NO RDAP    = that TLD publishes no RDAP service. Never checked;")
        print("             not a statement about the domain. Check by hand.")
    if "UNKNOWN" in seen:
        print("UNKNOWN    = registry unreachable, rate-limited, or not answering")
        print("             RDAP. Check manually at a registrar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
