#!/usr/bin/env python3
"""
subdomain_enum.py
Simple, safe subdomain enumeration helper.
Uses public cert transparency (crt.sh) and DNS bruteforce (optional small wordlist).
Educational only. Do not use for abusive scanning.
"""

import argparse
import requests
import dns.resolver
from concurrent.futures import ThreadPoolExecutor, as_completed

CRT_SH_URL = "https://crt.sh/?q=%25.{domain}&output=json"

def crtsh_subdomains(domain):
    url = CRT_SH_URL.format(domain=domain)
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        subs = set()
        for entry in data:
            name = entry.get("name_value", "")
            for part in name.splitlines():
                part = part.strip()
                if part:
                    subs.add(part.lstrip("*."))
        return sorted(subs)
    except Exception:
        return []

def dns_resolve(host):
    try:
        answers = dns.resolver.resolve(host, "A", lifetime=5)
        return host, [r.to_text() for r in answers]
    except Exception:
        return host, []

def brute_force(domain, wordlist, threads=8):
    candidates = [f"{w.strip()}.{domain}" for w in wordlist if w.strip()]
    found = {}
    with ThreadPoolExecutor(max_workers=threads) as exe:
        futures = {exe.submit(dns_resolve, c): c for c in candidates}
        for fut in as_completed(futures):
            host, ips = fut.result()
            if ips:
                found[host] = ips
    return found

def load_wordlist(path):
    with open(path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() and not l.startswith("#")]

def main():
    parser = argparse.ArgumentParser(description="Subdomain enumeration (crt.sh + optional brute force)")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--brute", "-b", help="Optional wordlist for small brute force", default=None)
    parser.add_argument("--threads", "-t", help="Threads for DNS checks", type=int, default=8)
    args = parser.parse_args()

    domain = args.domain
    print(f"[+] Querying crt.sh for {domain}")
    crt_subs = crtsh_subdomains(domain)
    for s in crt_subs:
        print(s)
    print(f"[+] Found {len(crt_subs)} unique names via crt.sh")

    if args.brute:
        print(f"[+] Running small brute force using {args.brute}")
        wl = load_wordlist(args.brute)
        results = brute_force(domain, wl, threads=args.threads)
        for host, ips in results.items():
            print(f"{host} -> {', '.join(ips)}")
        print(f"[+] Brute force discovered {len(results)} hosts")

if __name__ == "__main__":
    main()

