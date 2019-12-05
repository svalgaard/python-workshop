#! /usr/bin/env python3
#
# Replace Windows line breaks with \n
#

import os
import sys
import tempfile


def usage():
    print('Usage:')
    print('    win2unix [options] [file1 [file2 [...]]]')
    print()
    print('Options:')
    print('    -h  Print this help message')
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if '-h' in args or '--help' in args or not args:
        usage()

    for arg in args:
        tempfile.tempdir = os.path.dirname(arg)
        tempname = tempfile.mktemp()
        data = open(arg, 'rb').read()
        data2 = data.replace(b'\r\n', b'\n')
        if data != data2:
            open(tempname, 'wb').write(data)
            os.rename(tempname, arg)


if __name__ == '__main__':
    main()
