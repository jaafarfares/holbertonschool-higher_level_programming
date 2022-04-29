#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in range(len(argv) - 1):
        s = int(argv[i] + 1)
        if s == 1:
            print("{}".format(s - 1))
        else:
            print("{}".format(s))
