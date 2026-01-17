#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    i = 1
    while i <= n:
        print("{}: {}".format(i, sys.argv[i]))

        i += 1
