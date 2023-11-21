#!/usr/bin/python3
"""Square module."""


class Square:
    """Square module."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of a square.
        """
        self.__size = size
    @property
    def size(self):
        """ Proprty for the lenght

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less then 0
        """
        return self.__size = size

    @size.setter
    def size(self, value):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = Value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2
