#!/usr/bin/python3
"""Write a function that writes a string
to a text file (UTF8) and returns the
number of characters written:"""


def write_file(filename="", text=""):
    """the function parameter to open the file and write the string"""
    with open(filename, 'w', encoding='utf-8') as f:
        s = str(text)
        f.write(s)
        return len(text)
