#!/usr/bin/python3
"""
read a txt file 
"""

def read_file(filename=""):
    """read_file is function that read a txt file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
