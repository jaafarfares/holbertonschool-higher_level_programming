#!/usr/bin/python3
""" the program that
Iterate over a string to
serach for a special
charachter
"""


def text_indentation(text):
    """the function that checks for
    charachters and chek if
    the value is a string"""
    if not isinstance(text, (str)):
        raise(TypeError("text must be a string"))
    a = 0
    for i in text:
        if i == " " and a == 0:
            continue
        a = 1
        if a == 1:
            if i == "." or i == "?" or i == ":":
                print(f"{i}\n")
                a = 0
            else:
                print(i, end="")
