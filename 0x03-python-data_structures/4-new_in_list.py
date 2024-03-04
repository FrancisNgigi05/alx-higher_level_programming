#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    shallow_copy_list = my_list.copy()
    list_len = len(shallow_copy_list)

    if idx < 0:
        return my_list
    elif idx > list_len - 1:
        return my_list
    else:
        shallow_copy_list[idx] = element
        return shallow_copy_list
