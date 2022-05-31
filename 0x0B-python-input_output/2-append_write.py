#!/usr/bin/python3
"""Write a function that writes a string
to a text file (UTF8) and returns the
number of characters written:"""


def append_write(filename="", text=""):
    """the function parameter to open the file and write the string"""
    with open('file_append.txt', 'a', encoding='utf-8') as f:
        return (f.write(str(text)))
