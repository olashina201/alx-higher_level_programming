#!/usr/bin/python3

"""Define a class named Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.
        
        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
