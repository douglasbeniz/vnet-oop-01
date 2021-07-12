#!/usr/bin/python3

"""
source: https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
"""


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(7,6)
print(p.distanceFromOrigin())


