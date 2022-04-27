#!/usr/bin/python3
def fizzbuzz():
    for count in range(100):
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz", end=" ")
            continue
        elif count % 3 == 0:
            print("Fizz", end=" ")
            continue
        elif count % 5 == 0:
            print("Buzz", end=" ")
            continue
        print("{} ".format(count), end="")
