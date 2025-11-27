#!/usr/bin/env python3
"""
recon_harvester.py
Lightweight recon aggregator.
Collects data from public crt.sh and does basic enrichment:
- subdomains from crt.sh
- simple whois via public service (optional)
Output: JSON printed to stdout for easy piping to files.
Educational only.
"""

import argparse
import json
import requests
import socket

CRT_SH_URL = "https://crt.sh/?q=%25.{domain}&output=json"
WHOIS_API = "https://rdap.org/domain/{domain}"  # public RDAP endpoint

def get_crtsh(domain):
    try:
        r = requests.get(CRT_SH_URL.format(domain=domain), timeout=15)
        r.raise_for_status()
        data = r.json()
        subs = set()
        for entry in data:
            name = entry.get("name_value", "")
            for part in name.splitlines():
                subs.add(part.lstrip("*."))
        return sorted(subs)
    except Exception:
        return []

def rdap_lookup(domain):
    try:
        r = requests.get(WHOIS_API.format(domain=domain), timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {}

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return None

def enrich_subdomains(subs):
    enriched = {}
    for s in subs:
        try:
            ips = requests.get(f"https://dns.google/resolve?name={s}&type=A", timeout=8).json()
            answers = [a['data'] for a in ips.get('Answer', []) if a.get('type') == 1]
        except Exception:
            answers = []
        enriched[s] = answers
    return enriched

def main():
    parser = argparse.ArgumentParser(description="Recon Harvester - aggregate public recon data")
    parser.add_argument("domain", help="Target domain")
    args = parser.parse_args()

    domain = args.domain
    result = {"domain": domain, "subdomains": [], "subdomain_enrichment": {}, "rdap": {}}

    subs = get_crtsh(domain)
    result["subdomains"] = subs

    if subs:
        result["subdomain_enrichment"] = enrich_subdomains(subs[:50])  # limit to first 50 for speed

    rdap = rdap_lookup(domain)
    result["rdap"] = rdap

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

