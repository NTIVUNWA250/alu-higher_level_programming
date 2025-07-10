#!/usr/bin/python3
"""
This module defines a class  Rectangle with width and height.
The class provides methods to check the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    Defines a rect by its width and height,methods for area and perimeter.
    Attributes:
        width (int): The width of the rectangle, must be >= 0.
        height (int): The height of the rectangle, must be >= 0.

    Methods:
        width (int): Gets or sets the width of the rectangle.
        height (int): Gets or sets the height of the rectangle.
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with an optional width and height.
        Args:
            width (int: The width of the rect
            height (int): The height of the rect
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
        Sets the width of the rct  with validation.
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

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
                 Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
