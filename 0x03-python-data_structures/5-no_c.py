#!/usr/bin/python3
def no_c(my_string):
    edited_string = ""
    string_len = len(my_string)

    for letter in range(string_len):
        if my_string[letter] != "c" and my_string[letter] != "C":
            edited_string += my_string[letter]

    return edited_string
