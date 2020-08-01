'''
Author: Josh Birlingmair
Date:   7/8/2020
'''

import sys
import random

class Point:
    EPSILON = 1.0e-5    # Value close enough to zero for evaluating to points' x, y, and z values

    def __hash__(self):
        x = int(self.x)
        y = int(self.y)
        z = int(self.z)
        s = int(self.x**2 + self.y**2 + self.z**2)

        return int(f'{x}{y}{z}{s}')

    def __init__(self, x = None, y = None, z = None):
        if x == None and y == None:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
        elif z == None:
            raise SyntaxError('Error: Point needs an x, y, and z value')
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __eq__(self, p):
        if isinstance(p, Point):
            dx = abs(self.x - p.x)
            dy = abs(self.y - p.y)
            dz = abs(self.z - p.z)

            if dx < Point.EPSILON and dy < Point.EPSILON and dz < Point.EPSILON:
                return True
            else: return False
        else:
            return False

    def __ne__(self, p):
        return not self.__eq__(p)

    def euclid_dist(self, p):
        dx = abs(self.x - p.x)
        dy = abs(self.y - p.y)
        dz = abs(self.z - p.z)

        return (dx**2 + dy**2 + dz**2) ** 0.5

class Cloud:
    def __init__(self):
        self.points = set()

    def __str__(self):
        return '[' + ', '.join(map(str, self.points)) + ']'

    def is_empty(self):
        return len(self.points) == 0

    def size(self):
        return len(self.points)

    def has_point(self, p):
        for point in self.points:
            if p.x == point.x and p.y == point.y and p.z == point.z:
                return True
        return False

    def add_point(self, p):
        if not self.has_point(p):
            self.points.add(p)

    # Returns an array of extremes: left, right, top, and bottom of all points in cloud
    # If cloud is empty, returns None
    def extremes(self):
        if self.is_empty: return None
        
        cloud = self.points
        min_x = max_x = min_y = max_y = max_z = min_z = random.choice(cloud)

        for p in cloud:
            if p.x < min_x:
                min_x = p.x
            if p.x > max_x:
                max_x = p.x

            if p.y > max_y:
                max_x = p.x
            if p.y < min_y:
                min_y = p.y

            if p.z > max_z:
                max_z = p.z
            if p.z < min_z:
                min_z = p.z

        return [min_x, max_x, max_y, min_y, max_z, min_z]

    # If cloud is not empty create and return the center point
    # else return null;
    def center_p(self):
        if self.is_empty():
            return None

        cloud = self.points
        total_x = total_y = total_z = 0

        for p in cloud:
            total_x += p.x
        avg_x = total_x / len(cloud)

        for p in cloud:
            total_y += p.y
        avg_y = total_y / len(cloud)

        for p in cloud:
            total_z += p.z
        avg_z = total_z / len(cloud)

        return Point(avg_x, avg_y, avg_z)

    # Returns minimal distance between 2 points in the cloud
	# Returns 0.0 for a cloud with less than 2 points
    def min_dist(self):
        if self.size() < 2: return 0.0

        cloud = self.points
        min_dist = float(sys.maxsize)

        for p0 in cloud:
            for p1 in cloud:
                if p0.euclid_dist(p1) < min_dist and p0 != p1:
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

        if p0.get_z() < p1.get_z():
            min_z = p0.get_z()
            max_z = p1.get_z()
        else:
            min_z = p1.get_z()
            max_z = p0.get_z()

        cloud = self.points
        for p in cloud:
            if p.get_x() < min_x or p.get_x() > max_x:
                cloud.remove(p)
            if p.get_y() < min_y or p.get_y() > max_y:
                cloud.remove(p)
            if p.get_z() < min_z or p.get_z() > max_z:
                cloud.remove(p)

####################
# TEST POINT CLASS #
####################

debug_point = False
if debug_point:
    print('Point class debug ON')
    print(f'EPSILON: {Point.EPSILON}')

    origin  = Point()
    p1      = Point(0.0, 4.0, 4.0)
    p2      = Point(3.0000001, 3.9999999, 3.9999999)
    p3      = Point(3.0, 4.0, 4.0)
    p4      = Point(0.0, 5.0, 5.0)
    p5      = Point(12.0, 0.0, 0.0)

    print(f'origin: {origin}')
    print(f'p1: {p1}')
    print(f'p2: {p2}')
    print(f'p3: {p3}')
    print(f'p4: {p4}')
    print(f'p5: {p5}')

    if p2 == p3:
        print(f'{p2} equals {p3}')
    else:
        print(f'{p2} does not equal {p3}')

    print(f'Euclidean distance between {origin} and {p1}: {origin.euclid_dist(p1)}')
    print(f'Euclidean distance between {p1} and {p3}: {p1.euclid_dist(p3)}')
    print(f'Euclidean distance between {origin} and {p3}: {origin.euclid_dist(p3)}')
    print(f'Euclidean distance between {p4} and {p5}: {p4.euclid_dist(p5)}')
else:
    print('Point class debug OFF')

####################
# TEST CLOUD CLASS #
####################

debug_cloud = True
if debug_cloud:
    cloud = Cloud()

    print('Cloud class debug ON')
    print(f'Cloud: {cloud}')

    if not cloud.is_empty():
        print('Error: cloud should be empty!')

    if cloud.extremes != None:
        print('Error: extremes should be None!')

    if cloud.min_dist() != 0.0:
        print('Error: min_dist should return 0.0!')

    p311 = Point(3.0, 1.0, 1.0)
    cloud.add_point(p311)

    p222 = Point(2.0, 2.0, 2.0)
    cloud.add_point(p222)

    p422 = Point(4.0, 2.0, 2.0)
    cloud.add_point(p422)

    p333 = Point(3.0, 3.0, 3.0)
    cloud.add_point(p333)

    print(f'Cloud 1: {cloud}')
    print(f'Center point in cloud: {cloud.center_p()}')
    print(f'Cloud: {cloud}')
    print(f'Cloud 2: {cloud}')

    p777 = Point(7, 7, 7)
    if cloud.has_point(p777):
        print(f'Error: point {p777} should not be in cloud')
    else:
        print(f'OK: point {p777} not in cloud')
    
    extrs = cloud.extremes()
    if(extrs != None):
        print(f'Left: {extrs[0]}')
        print(f'Right: {extrs[1]}')
        print(f'Top: {extrs[2]}')
        print(f'Bottom: {extrs[3]}')
    
    print('Min dist in cloud: {:.5f}'.format(cloud.min_dist()))

    print('Test cloud with one point')

    cloud1 = Cloud()
    p = Point()
    cloud1.add_point(p)

    print('Min dist in cloud1: {:.5f}'.format(cloud1.min_dist()))
else:
    print('Cloud class debug OFF')
