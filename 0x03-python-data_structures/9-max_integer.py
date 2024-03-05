#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = my_list[0]
    if not my_list:
        return None
    for number in range(len(my_list) - 1):
        if max_num < my_list[number]:
            max_num = my_list[number]
    return max_num
