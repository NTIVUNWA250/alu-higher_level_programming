#!/usr/bin/python3
"""
print_square module
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
