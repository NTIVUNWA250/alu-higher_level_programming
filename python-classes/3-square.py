#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute `size`,
includes validation for `size`, and a method to compute it's areaS.
"""


class Square:
    """
    Represents a square with a validated size.

    Attributes:
        __size (int): The size of a side of the square. Must be an integer
                      and >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
