#!/usr/bin/python3

"""
source: https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
"""


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(Point)
print(p)
print(q)

print(p is q)

