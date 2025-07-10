#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
as well as methods to calculate area, perimeter, and compare rectangles
by area.
"""


class Rectangle:
    """
    Represents a rectangle with width and height attributes, and includes
    methods for area, perimeter, and comparison of rectangles.

    Attributes:
        width (int): The width of the rectangle, must be >= 0.
        height (int): The height of the rectangle, must be >= 0.
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for the visual representation.

    Methods:
        width (int): Gets or sets the width of the rectangle.
        height (int): Gets or sets the height of the rectangle.
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        bigger_or_equal(rect_1, rect_2): Returns the rect with large area
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with an optional width and height.
        Increments the number_of_instances class attribute.
        Args:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Returns a string representation of the rectangle using the
        `print_symbol` character.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns an eval-compatible string representation of the rectangle.

        This representation allows for the creation of a new instance
        using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        and decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the greater area.
        If both have the same area, returns rect_1.

        Args:
            rect_1 (Rectangle): First rectangle instance.
            rect_2 (Rectangle): Second rectangle instance.

        Raises:
            TypeError: If either rect_1 or rect_2 isn't instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the greater or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
