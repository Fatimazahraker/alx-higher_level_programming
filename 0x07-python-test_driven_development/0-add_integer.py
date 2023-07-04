#!/usr/bin/python3
""" function that adds 2 integers. """


def add_integer(a, b=98):
    """
    function that add a and b
    if a or b not int or float, TypeError raise
    """

    # Check if a not int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # check if b not int pr float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a,b to ints and return the sum
    return int(a) + int(b)
