import argparse, json
from pathlib import Path
from .core import scan

def main():
    ap = argparse.ArgumentParser(prog="a11y-scout")
    ap.add_argument("url")
    ap.add_argument("--out", type=Path, help="write JSON report")
    args = ap.parse_args()
    data = scan(args.url, args.out)
    print(f"violations: {len(data['violations'])}")
    if not args.out:
        print(json.dumps(data['violations'][:3], indent=2))  # preview
if __name__ == "__main__":
    main()
