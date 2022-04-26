#!/usr/bin/env python3
def fizzbuzz():
    for fiz in range(51):
        if fiz % 3 == 0 and fiz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fiz % 3 == 0:
            print("fizz")
            continue
        elif fiz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)
