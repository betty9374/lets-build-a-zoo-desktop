"""Lets Build a Zoo Desktop — A local helper for Let's Build a Zoo park folders, exhibit files, and visitor photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='lets_build_a_zoo_desktop',
        description="A local helper for Let's Build a Zoo park folders, exhibit files, and visitor photos.",
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Lets Build a Zoo Desktop')
    print('Keep the park on disk before a gene update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
