#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_length = len(sys.argv)
    add = 0

    for i in range(1, argv_length):
        add += int(sys.argv[i])
    print("{}".format(add))
