#!/usr/bin/python3
for i in range(0, 9):
    for a in range(0, 10):
        if i == 8 and a == 9:
            print("{:d}{:d}\n".format(i, a))
        elif a > i:
            print("{:d}{:d}".format(i, a), end=", ")
