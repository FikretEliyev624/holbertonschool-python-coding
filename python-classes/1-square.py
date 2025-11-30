#!/usr/bin/python3
"""
1-square module

"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """Initialize a square with a private size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
