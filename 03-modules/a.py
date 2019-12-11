#! /usr/bin/env python3
# a.py
#
import sys
import sub.b
import c


print("In a.py")


def main():
    print('In a.py main()')

    print(f'sys.argv : {sys.argv}')
    print(f'sub.b.var: {sub.b.var}')
    print(f'c.var    : {c.var}')


if __name__ == '__main__':
    # Only run main() if this is file is NOT imported
    main()
