#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    elif len(argv) > 1:
        sum = 0
        for i in range(1, len(argv)):
            sum+= int(argv[i])
        print(sum)
