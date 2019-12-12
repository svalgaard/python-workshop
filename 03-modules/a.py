#! /usr/bin/env python3
# a.py
#
import sys
import sub.subsub.d
import sub.b
import c


print("In a.py")


def main():
    print('In a.py main()')

    print()
    print(f'sys.argv        : {sys.argv}')
    print(f'sub.b.var       : {sub.b.var}')
    print(f'c.var           : {c.var}')
    print(f'sub.subsub.d.var: {sub.subsub.d.var}')


if __name__ == '__main__':
    # Only run main() if this is file is NOT imported
    main()
