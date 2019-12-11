#
# sub/b.py
#

print("In c.py")


def main():
    print('In c.py main()')


var = 42

if __name__ == '__main__':
    # Only run main() if this is file is NOT imported
    main()
