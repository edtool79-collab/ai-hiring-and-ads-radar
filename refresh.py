#!/usr/bin/env python3
"""Refresh the HirePulse hiring/ads radar table.

Each domain costs one free HirePulse call (5 per UTC day per IP, shared).
No account, no API key. After the free calls the API answers 402 with x402
payment terms; this script never pays and just records the 402.

Usage: python refresh.py linear.app ramp.com stripe.com
"""
import json, os, sys, urllib.request, urllib.error, datetime

API = "https://gethirepulse.xyz/v1/company-profile"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def fetch(domain: str):
    body = json.dumps({"domain": domain}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:400]}


def main(domains):
    os.makedirs(DATA, exist_ok=True)
    for d in domains:
        code, payload = fetch(d)
        print(d, code)
        if code == 200:
            json.dump(payload, open(os.path.join(DATA, d + ".json"), "w", encoding="utf-8"), indent=2)
        else:
            print("  not stored:", json.dumps(payload)[:160])
    print("done", datetime.datetime.utcnow().isoformat(), "UTC — rebuild the table with scripts/build_table.py")


if __name__ == "__main__":
    main(sys.argv[1:] or ["linear.app"])
