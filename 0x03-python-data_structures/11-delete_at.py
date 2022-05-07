#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = (len(my_list) - 1)
    if idx < 0:
        return my_list
    elif idx > i:
        return my_list
    else:
        my_list.remove(my_list[idx])
    return my_list
