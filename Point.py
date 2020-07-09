import sys

debug = False

class Point:
    EPSILON = 1e-5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def toString(self):
        str = '({x}, {y})'.format(self.x, self.y)
        return str

class Cloud:
    def __init__(self):
        cloud = []