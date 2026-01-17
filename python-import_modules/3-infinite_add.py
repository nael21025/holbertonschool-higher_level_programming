#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0

    i = 1
    while i < len(sys.argv):
        total = total + int(sys.argv[i])
        i += 1

    print(total)
