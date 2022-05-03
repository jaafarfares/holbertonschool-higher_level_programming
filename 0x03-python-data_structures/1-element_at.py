#!/usr/bin/python3
def element_at(my_list, idx):
    a = my_list
    i = idx
    if i < 0 or i > (len(a) - 1):
        return None
    return(a[i])
