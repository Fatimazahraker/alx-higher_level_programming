#!/usr/bin/python3
""" module doc"""
from models.base import Base


class Rectangle(Base):
    """ class doc """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width doc """
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ height doc """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ x doc """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ y doc """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

