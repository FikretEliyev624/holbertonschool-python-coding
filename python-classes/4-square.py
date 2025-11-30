#!/usr/bin/python3
"""
4-square module

"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize a square with a private size attribute"""
        self.__size = size

    @property
    def size(self):
        """Retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size**2

    def my_print(self):
        """that prints in stdout the square with the character"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
