#!/usr/bin/python3
"""
The  module defines a class Rectangle with width and height.
The class ensures that both attributes are int >=  to 0.
"""


class Rectangle:
    """
    Defines a rectangle by its width and height.
    Attributes:
        width (int): The width of the rectangle. Must be >= 0.
        height (int): The height of the rectangle. Must be >= 0.
    Methods:
        width (int): Gets or sets the width of the rectangle.
        height (int): Gets or sets the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.
        Args:
            value (int): The new width of the rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.
        Args:
            value (int): The new height of the rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
