#!/usr/bin/python3

"""
source: https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
"""

import math 

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

    def __str__(self):
        return "p(x:%s, y:%s)" % (self.x, self.y)


def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

# Object 1
p = Point(4,3)
q = Point(0,0)
print("Distance from %s to origin, method 1: %f" % (str(p), distance(p,q)))

p = Point(4,3)
#print(p.distanceFromOrigin())
print("Distance from %s to origin, method 1: %f" % (str(p), p.distanceFromOrigin()))

# Object 2
p = Point(7,6)
q = Point(0,0)
print("Distance from %s to origin, method 1: %f" % (str(p), distance(p,q)))

p = Point(7,6)
#print(p.distanceFromOrigin())
print("Distance from %s to origin, method 1: %f" % (str(p), p.distanceFromOrigin()))
