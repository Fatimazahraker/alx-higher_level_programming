#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        separate = ", "
        if i == 8:
            separate = "\n"
        print("{:d}{:d}".format(i, j), end=separate)
