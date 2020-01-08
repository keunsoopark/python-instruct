import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x  # data attribute
        self.y = y

    def distance_from_origin(self):  # method attribute
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # __repr__ method can manipulate what is printed as Point instance is typed.
    # Without this, Python default one is printed (ex. <ShapeClass.Point object at 0x105b39e10>)
    def __repr__(self):
        return "point ({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)  # construct & initialize -> now Circle's self.x = x
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)  # distance_from_origin() is also already inherited.

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super.__eq__(other)

    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)

    def __str__(self):
        return repr(self)
