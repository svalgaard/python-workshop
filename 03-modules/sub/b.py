#
# sub/b.py
#

print("In sub/b.py")


def main():
    print('In sub/b.py main()')


var = 7

if __name__ == '__main__':
    # Only run main() if this is file is NOT imported
    main()
