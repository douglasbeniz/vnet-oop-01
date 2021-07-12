#!/usr/bin/python3

"""
source: https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
"""


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

p = Point(7,6)
