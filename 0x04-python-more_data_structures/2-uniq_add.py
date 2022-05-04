#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = set(my_list)
    a = 0
    for i in num:
        a = a + i
    return a
