#! /usr/bin/env python3
#
# Minimal example with argparse
# https://docs.python.org/3/howto/argparse.html

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")

    args = parser.parse_args()

    if args.verbose:
        print(args)

    answer = args.x**args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} == {answer}")


if __name__ == '__main__':
    main()
