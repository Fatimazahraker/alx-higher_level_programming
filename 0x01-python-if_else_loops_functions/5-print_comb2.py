#!/usr/bin/python3
for number in range(0, 100):
    separate = ", "
    if number == 99:
        separate = "\n"
    print("{:02d}".format(number), end=separate)
