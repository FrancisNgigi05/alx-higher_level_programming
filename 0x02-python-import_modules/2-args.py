#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_length = len(sys.argv)

    if argv_length < 2:
        print("0 arguments.")

    elif argv_length == 2 and argv_length < 3:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(argv_length - 1))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
