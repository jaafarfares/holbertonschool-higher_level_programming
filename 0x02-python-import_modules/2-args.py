#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        a = argv[1]
        print(f"1 argument:")
        print(f"1: {a}")
    if len(argv) > 2:
        print(f"{len(argv) -1} arguments:")
        for i in range(1, len(argv)):
            #print(i)
            print(f"{i}: {argv[i]}")
