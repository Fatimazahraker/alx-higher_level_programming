#!/usr/bin/python3
""" module doc"""


class Base:
    """ class doc """
    __nb_objects = 0

    def __init__(self, id=None):
        """ intitialisation of base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
