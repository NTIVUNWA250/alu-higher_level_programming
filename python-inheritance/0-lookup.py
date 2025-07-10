#!/usr/bin/python3
"""
This module defines a function `lookup` that returns a list of all available
attributes and methods of an object using the built-in `dir()` function.
"""


def lookup(obj):
    """
    Returns a list of available attrib and methods of an obj.
    Args:
        obj:obj whose attributes and methods are to be retrieved.
    Returns:
        A list of the object's attributes and methods.
    """
    return dir(obj)
