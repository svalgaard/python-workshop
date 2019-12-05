#! /usr/bin/env python3
#
# Requires requests
#

import subprocess
import sys


def main():
    # This is very dangerous as we trust user input
    cmd = ['ls', '-ald'] + sys.argv[1:]

    print(f'Running this command: {" ".join(cmd)}')

    try:
        # capture stdout (not stderr) in output
        output = subprocess.check_output(cmd)

        # output is a byte sequence
        output = output.decode('utf-8')

        print(output.upper())
    except subprocess.CalledProcessError as err:
        print('Running command failed')
        raise err


if __name__ == '__main__':
    main()
