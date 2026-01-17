#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        endc = ", " if not (i == 8 and j == 9) else "\n"
        print("{:d}{:d}".format(i, j), end=endc)
