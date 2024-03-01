#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            upper_case_char = chr(ord(letter) - 32)
        else:
            upper_case_char = letter

        print("{}".format(upper_case_char), end="")

    print()
