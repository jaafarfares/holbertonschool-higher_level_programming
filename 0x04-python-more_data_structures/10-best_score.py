#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = next(iter(a_dictionary))
    b = a_dictionary.get(a)
    for key, integer_value in a_dictionary.items():
        if integer_value > b:
            b = integer_value
            a = key
    return a
