debug_point = False
debug_cloud = False
EPSILON     = 1e-5

class Point:
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

    def __eq__(self, p):    # TODO Add feature for if p is not a point
        if abs(self.x - p.x) < EPSILON and abs(self.y - p.y) < EPSILON:
            return True
        else: return False

    def euclid_dist(self, p):
        dx = abs(self.x - p.x)
        dy = abs(self.y - p.y)

        return (dy**2 + dy**2) ** 0.5

class Cloud:
    def __init__(self):
        self.cloud = set()

####################
# TEST POINT CLASS #
####################

debug_point = True
if debug_point:
    p0 = Point(0.0, 0.0)
    p1 = Point(0.0, 0.1)

    print(p0 == p1)

####################
# TEST CLOUD CLASS #
####################

# debug_cloud = False
# if debug_cloud:
#     print("Hello world")