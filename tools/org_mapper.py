#!/usr/bin/env python3
"""
org_mapper.py
Build a simple organization map from a domain and its discovered subdomains.
Outputs a Graphviz DOT file and a small JSON adjacency list.
Educational only. No scanning, only enrichment of public data.
"""

import argparse
import json
import subprocess
from collections import defaultdict

# Reuse the recon harvester's approach but keep this file standalone and simple.
import requests

CRT_SH_URL = "https://crt.sh/?q=%25.{domain}&output=json"
DNS_GOOGLE = "https://dns.google/resolve?name={name}&type=A"

def get_subdomains(domain):
    try:
        r = requests.get(CRT_SH_URL.format(domain=domain), timeout=15)
        r.raise_for_status()
        data = r.json()
        subs = set()
        for e in data:
            name = e.get("name_value", "")
            for part in name.splitlines():
                subs.add(part.lstrip("*."))
        return sorted(subs)
    except Exception:
        return []

def resolve_a(name):
    try:
        r = requests.get(DNS_GOOGLE.format(name=name), timeout=8).json()
        answers = [a['data'] for a in r.get('Answer', []) if a.get('type') == 1]
        return answers
    except Exception:
        return []

def build_graph(domain, subdomains, limit=100):
    nodes = set([domain])
    edges = []
    adj = defaultdict(list)

    count = 0
    for s in subdomains:
        if count >= limit:
            break
        nodes.add(s)
        ips = resolve_a(s)
        for ip in ips:
            node_ip = f"ip:{ip}"
            nodes.add(node_ip)
            edges.append((s, node_ip))
            adj[s].append(node_ip)
        # link subdomain to root domain for a simple org relation
        edges.append((domain, s))
        adj[domain].append(s)
        count += 1

    return nodes, edges, adj

def write_dot(nodes, edges, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("digraph orgmap {\n")
        for n in nodes:
            label = n.replace('"', '\\"')
            f.write(f'  "{label}";\n')
        for a, b in edges:
            aa = a.replace('"', '\\"')
            bb = b.replace('"', '\\"')
            f.write(f'  "{aa}" -> "{bb}";\n')
        f.write("}\n")

def main():
    parser = argparse.ArgumentParser(description="Org mapper - create simple org map from domain")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--limit", "-l", type=int, default=200, help="Max subdomains to process")
    parser.add_argument("--dot", default="orgmap.dot", help="Output DOT filename")
    parser.add_argument("--json", default="orgmap.json", help="Output JSON filename")
    args = parser.parse_args()

    subs = get_subdomains(args.domain)
    nodes, edges, adj = build_graph(args.domain, subs, limit=args.limit)

    write_dot(nodes, edges, args.dot)
    with open(args.json, "w", encoding="utf-8") as jf:
        json.dump({"nodes": list(nodes), "edges": edges, "adj": adj}, jf, indent=2, ensure_ascii=False)

    print(f"[+] Subdomains discovered: {len(subs)} (limited to {args.limit})")
    print(f"[+] DOT written to {args.dot}")
    print(f"[+] JSON written to {args.json}")
    print("[+] You can render the DOT with Graphviz: dot -Tpng orgmap.dot -o orgmap.png")

if __name__ == "__main__":
    main()

