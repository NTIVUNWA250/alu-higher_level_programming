#!/usr/bin/python3
"""
The module defines a class  Rectangle with width and height.
The class provides methods for checking area, perimeter
representation, and an eval-compatible representation.
"""


class Rectangle:
    """
    Defines a rectangle by its width and height, with methods for area,
    perimeter, a visual string representation, and an eval-compatible
    representation.
    Attributes:
        width (int): The width of the rectangle, must be >= 0.
        height (int): The height of the rectangle, must be >= 0.
    Methods:
        width (int): Gets or sets the width of the rectangle.
        height (int): Gets or sets the height of the rectangle.
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle.
        __repr__(): Returns an eval-compatible string representation.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with an optional width and height.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the `#`
        character.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns an eval-compatible string representation of the rectangle.
        This representation allows for the creation of a new instance
        using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
