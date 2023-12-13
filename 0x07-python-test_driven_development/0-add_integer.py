#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=99):
    """adds two intergers

    Args:
        a: the fisrt interger
        b: the second integer, default 98

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of two intergers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b mst be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
