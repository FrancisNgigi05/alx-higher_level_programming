#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv_length = len(sys.argv)

    if argv_length < 2:
        print("0 argument.")
    elif argv_length == 2:
        print("1 argument:")
    else:
        print("{} arguments".format(argv_length - 1))
    for i in range(1, argv_length):
         print("{}: {}".format(i, sys.argv[i]))
