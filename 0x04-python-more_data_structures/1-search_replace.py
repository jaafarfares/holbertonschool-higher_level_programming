#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = 0
    newList = my_list.copy()
    for n in newList:
        if n == search:
            newList[a] = replace
        a = a + 1
    return newList
