#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """reads file name with utf8"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end="")
