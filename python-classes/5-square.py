#!/usr/bin/python3
"""
This module defines a Square class wid validation for sze, method to compute
the it's area with method to print the square using the character "#".
"""


class Square:
    """
    Represents a square with a validated size and a method to print the square.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character "#" for each row and column.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
