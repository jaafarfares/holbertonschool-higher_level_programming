#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = str
    if n >= 0:
        new_string = new_string[:n] + new_string[n+1:]
    return new_string
