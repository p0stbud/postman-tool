#!/usr/bin/env python3
import argparse
from tools import menu


def main():
    parser = argparse.ArgumentParser(description="POSTMAN-TOOL - Automate your data tasks")
    subparsers = parser.add_subparsers(dest='tool', help='Tool to use.')

    time_converter = subparsers.add_parser('time-converter', help='Convert time to proper form for polish zone')
    time_converter.add_argument('-p', '--path', type=str, help='Point the path to convert.', metavar='PATH')

    hasher = subparsers.add_parser('hasher', help='Get proper hash for file or files.')
    hasher.add_argument('-t', '--type', type=str, choices=[
                                                                         'ed2k',
                                                                         'SHA1_base32',
                                                                         'MD4'],
                        nargs='*', default=['ed2k', 'SHA1_base32'], help='Use for get the chosen hash or hashes.')
    hasher.add_argument('-p', '--path', type=str, help='Point the path to get hashes.', metavar='PATH')

    researcher = subparsers.add_parser('researcher', help='Research chosen destination.')
    researcher.add_argument('-p', '--path', type=str, help='Point the path to research.', metavar='PATH')
    researcher.add_argument('-r', '--recursive', action='store_true', help='Use for recursive research.')

    args = parser.parse_args()

    try:
        menu[args.tool](args)
    except KeyError:
        print(f"Available tools: {', '.join(menu.keys())}")


if __name__ == "__main__":
    main()
