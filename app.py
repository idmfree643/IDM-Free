"""Command-line companion for the IDM Free safe-download guide."""

import argparse
import json

from checksum import sha256_file
from official_sources import ALTERNATIVE_PROJECTS, OFFICIAL_IDM_LINKS
from url_guard import is_official_idm_url


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Show official IDM links and verify URLs or file hashes."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("links", help="print official and alternative links")
    verify = subparsers.add_parser("verify-url", help="check an IDM URL")
    verify.add_argument("url")
    checksum = subparsers.add_parser("sha256", help="hash a local file")
    checksum.add_argument("path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "links":
        print(json.dumps({
            "official_idm": OFFICIAL_IDM_LINKS,
            "alternatives": ALTERNATIVE_PROJECTS,
        }, indent=2))
        return 0
    if args.command == "verify-url":
        trusted = is_official_idm_url(args.url)
        print("official" if trusted else "unverified")
        return 0 if trusted else 2
    print(sha256_file(args.path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
