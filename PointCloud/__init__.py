import sys

class Point:
    # Value close enough to zero for evaluating
    # two points' x, y, and z values
    EPSILON = 1.0e-5

    def __hash__(self):
        x = int(self.__x)
        y = int(self.__y)
        z = int(self.__z)
        s = int(self.__x**2 + self.__y**2 + self.__z**2)

        return int(f'{x}{y}{z}{s}')

    def __init__(self, x = None, y = None, z = None):
        if x == None and y == None:
            self.__x = 0.0
            self.__y = 0.0
            self.__z = 0.0
        elif z == None:
            raise SyntaxError('Error: Point needs an x, y, and z value')
        else:
            self.__x = x
            self.__y = y
            self.__z = z
    
    def __str__(self):
        return f'({self.__x}, {self.__y}, {self.__z})'

    def __eq__(self, p):
        if isinstance(p, Point):
            dx = abs(self.__x - p.__x)
            dy = abs(self.__y - p.__y)
            dz = abs(self.__z - p.__z)

            if dx < Point.EPSILON and dy < Point.EPSILON and dz < Point.EPSILON:
                return True
            else: return False
        else:
            return False

    def __ne__(self, p):
        return not self.__eq__(p)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def euclid_dist(self, p):
        dx = abs(self.__x - p.__x)
        dy = abs(self.__y - p.__y)
        dz = abs(self.__z - p.__z)

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
            if p.get_x() == point.get_x() and p.get_y() == point.get_y() and p.get_z() == point.get_z():
                return True
        return False

    def add_point(self, p):
        if not self.has_point(p):
            self.points.add(p)

    # Returns an array of extremes: left, right, top, and bottom of all points in cloud
    # If cloud is empty, returns None
    def extremes(self):
        if self.is_empty(): return None
        
        cloud = self.points
        point = list(cloud)[0]
        min_x = max_x = point.get_x()
        min_y = max_y = point.get_y()
        min_z = max_z = point.get_z()

        for p in cloud:
            if p.get_x() < min_x:
                min_x = p.get_x()
            if p.get_x() > max_x:
                max_x = p.get_x()

            if p.get_y() > max_y:
                max_y = p.get_y()
            if p.get_y() < min_y:
                min_y = p.get_y()

            if p.get_z() > max_z:
                max_z = p.get_z()
            if p.get_z() < min_z:
                min_z = p.get_z()

        return [min_x, max_x, max_y, min_y, max_z, min_z]

    # If cloud is not empty create and return the center point
    # else return null;
    def center_p(self):
        if self.is_empty(): return None

        cloud = self.points
        total_x = total_y = total_z = 0

        for p in cloud:
            total_x += p.get_x()
        avg_x = total_x / len(cloud)

        for p in cloud:
            total_y += p.get_y()
        avg_y = total_y / len(cloud)

        for p in cloud:
            total_z += p.get_z()
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
