#! /usr/bin/env python3
#
# Minimal example with sys.argv
#

import sys


def help():
    print(f'Usage: {sys.argv[0]} [-h] [-v] FILENAME [FILENAME]')
    sys.exit(1)


def main():
    args = sys.argv[1:]
    verbose = False
    if '-h' in args or '--help' in args:
        help()
    while '-v' in args:
        verbose = True
        args.remove('-v')

    filenames = args

    print(f'Verbose set to {verbose}')
    #
    # Do stuff on the files here
    #
    for fn in filenames:
        print(f'Looking at `{fn}`')


if __name__ == '__main__':
    # If this file is 'import'ed, main() is NOT run
    main()
