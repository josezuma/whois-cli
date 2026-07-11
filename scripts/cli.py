#!/usr/bin/env python3
"""whois-cli — WHOIS lookup CLI. Query domain registration information from public whois servers."""
import sys, json, argparse
def main():
    parser = argparse.ArgumentParser(description="WHOIS lookup CLI. Query domain registration information from public whois servers.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "whois-cli", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")
if __name__ == "__main__":
    main()
