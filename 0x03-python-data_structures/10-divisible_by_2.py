#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_listt = []
    for i in my_list:
        if i % 2 == 0:
            new_listt.append(True)
        else:
            new_listt.append(False)
    return new_listt
