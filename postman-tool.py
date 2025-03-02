#!/usr/bin/env python3
import argparse
from tools import menu


def main():
    parser = argparse.ArgumentParser(description="POSTMAN-TOOL - Automate your data tasks")
    subparsers = parser.add_subparsers(dest='tool', help='Tool to use.')
    researcher = subparsers.add_parser('researcher', help='Research chosen destination.')
    researcher.add_argument('-p', '--path', type=str, help='Point the path to research.', metavar='PATH')
    researcher.add_argument('-r', '--recursive', action='store_true', help='Use for recursive research.')
    hasher = subparsers.add_parser('hasher', help='Get proper hash of files.')
    hasher.add_argument('-t', '--type', type=str, choices=['ed2k',
                                                                         'SHA1_base32'], nargs='*',
                        default=['ed2k', 'SHA1_base32'], help='Use for get the chosen hash or hashes.')
    hasher.add_argument('-p', '--path', type=str, help='Point the path to get hashes.', metavar='PATH')
    args = parser.parse_args()

    if args.tool in menu.keys():
        menu[args.tool](args)
    else:
        print(f"tools to use: {', '.join(menu.keys())}")


if __name__ == "__main__":
    main()
