#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = my_list
    i = idx
    if i < 0 or i > (len(a) - 1):
        return None
    a[i] = element
    return (a)
