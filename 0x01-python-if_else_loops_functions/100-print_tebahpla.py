#!/usr/bin/python3
for alphabet in range(90, 64, -1):
    if alphabet % 2 == 0:
        alphabet += 32
    print(f"{chr(alphabet)}", end='')
