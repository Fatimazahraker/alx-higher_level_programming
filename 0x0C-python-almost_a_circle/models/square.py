#!/bin/usr/python3
""" module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class doc """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ doc """
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ strg representaion"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, 
                                        self.y, self.width)
