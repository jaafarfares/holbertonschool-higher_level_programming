#!/usr/bin/python3
def fizzbuzz():
    for count in range(100):
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print("fizzbuzz ", end="")
            continue
        elif count % 3 == 0:
            print("fizz ", end="")
            continue
        elif count % 5 == 0:
            print("buzz ", end="")
            continue
        print(count, " ", end="")
