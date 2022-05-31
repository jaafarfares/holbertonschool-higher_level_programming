#!/usr/bin/python3
""" a function that open  a file and write a text in it """


def append_write(filename="", text=""):
    """the function parameter to open the file and write the string"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
