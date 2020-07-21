import sys
import random

debug_point = False
debug_cloud = False

class Point:
    EPSILON = 1.0e-5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __eq__(self, p):    # TODO Add feature for if p is not a point
        if abs(self.x - p.x) < Point.EPSILON and abs(self.y - p.y) < Point.EPSILON:
            return True
        else: return False

    def euclid_dist(self, p):
        dx = abs(self.x - p.x)
        dy = abs(self.y - p.y)

        return (dx**2 + dy**2) ** 0.5

class Cloud:
    def __init__(self):
        self.points = set()

    def is_empty(self):
        return len(self.points) == 0

    def size(self):
        return len(self.points)

    def has_point(self, p):
        return p in self.points

    def add_point(self, p):
        if not self.has_point(p):
            self.points.add(p)

    # Returns an array of extremes: left, right, top, and bottom of all points in cloud
    # If cloud is empty, returns None
    def extremes(self):
        if self.is_empty: return None
        
        cloud = self.points
        min_x = max_x = min_y = max_y = random.choice(cloud)
        
        for p in cloud:
            if p.x < min_x:
                left = p.x

        for p in cloud:
            if p.x > max_x:
                right = p.x

        for p in cloud:
            if p.x > max_y:
                top = p.x

        for p in cloud:
            if p.x < min_y:
                bottom = p.x

        return [left, right, top, bottom]

    def center_p(self):
        cloud = self.points

        for p in cloud:
            total_x += p.x
        avg_x = total_x / len(cloud)

        for p in cloud:
            total_y += p.y
        avg_y = total_y / len(cloud)

        return Point(avg_x, avg_y)

    def min_dist(self):
        if self.size() < 2: return 0.0

        cloud = self.points
        min_dist = float(sys.maxsize)

        for p0 in cloud:
            for p1 in cloud:
                if p0.euclid_dist(p1) < min_dist:
                    min_dist = p0.euclid_dist(p1)

        return min_dist

    def crop(self, p0, p1):
        if p0.get_x() < p1.get_x():
            min_x = p0.get_x()
            max_x = p1.get_x()
        else:
            min_x = p1.get_x()
            max_x = p0.get_x()
        
        if p0.get_y() < p1.get_y():
            min_y = p0.get_y()
            max_y = p1.get_y()
        else:
            min_y = p1.get_y()
            max_y = p0.get_y()

        cloud = self.points
        for p in cloud:
            if p.get_x() < min_x or p.get_x() > max_x:
                cloud.remove(p)
            if p.get_y() < min_y or p.get_y() > max_y:
                cloud.remove(p)

####################
# TEST POINT CLASS #
####################

debug_point = False
if debug_point:
    print('Point class debug ON')
    print('EPSILON: {e}'.format(e = Point.EPSILON))

    origin  = Point(0.0, 0.0)
    p1      = Point(0.0, 4.0)
    p2      = Point(3.0000001, 3.9999999)
    p3      = Point(3.0, 4.0)
    p4      = Point(0.0, 5.0)
    p5      = Point(12.0, 0.0)

    print("origin: {p}".format(p=origin))
    print("p1: {p}".format(p=p1))
    print("p2: {p}".format(p=p2))
    print("p3: {p}".format(p=p3))
    print("p4: {p}".format(p=p4))
    print("p5: {p}".format(p=p5))

    if p2 == p3:
        print('{p2} equals {p3}'.format(p2=p2, p3=p3))
    else:
        print('{p2} does not equal {p3}'.format(p2=p2, p3=p3))

    print('Euclidean distance between {origin} and {p1}: {dist}'.format(origin=origin, p1=p1, dist=origin.euclid_dist(p1)))
    print('Euclidean distance between {p1} and {p3}: {dist}'.format(p1=p1, p3=p3, dist=p1.euclid_dist(p3)))
    print('Euclidean distance between {origin} and {p3}: {dist}'.format(origin=origin, p3=p3, dist=origin.euclid_dist(p3)))
    print('Euclidean distance between {p4} and {p5}: {dist}'.format(p4=p4, p5=p5, dist=p4.euclid_dist(p5)))
else:
    print('Point class debug OFF')

####################
# TEST CLOUD CLASS #
####################

# debug_cloud = False
# if debug_cloud:
#     print("Cloud class debug ON")
#     cloud = Cloud()