#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    for arguments in range(1, count):
        if count == 0:
            print("{} arguments.".format(count - 1))
        elif count == 1:
            print("{} argument: {}".format(count - 1, argv[arguments]))
        else:
            print("{} arguments: {}".format(count - 1, argv[arguments]))
