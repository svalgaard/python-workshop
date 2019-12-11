#
# a.py
#
import sys
import sub.b

print("In a.py")


def main():
    print('In a.py main()')

    print('sys.argv', sys.argv)
    print('sub.b', sub.b.var)


if __name__ == '__main__':
    # Only run main() if this is file is NOT imported
    main()
