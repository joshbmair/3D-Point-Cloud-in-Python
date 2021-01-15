import sys
from PointCloud import Point
from PointCloud import Cloud

# ######################################################################
# This is just a demonstration of all of the methods in the Point and  #
# Cloud classes. Feel free to edit/remove this file to use the methods #
# on your own.                                                         #
########################################################################

# TEST POINT CLASS

print(f'EPSILON: {Point.EPSILON}')

origin = Point()
p1     = Point(0.0, 4.0, 4.0)
p2     = Point(3.0000001, 3.9999999, 3.9999999)
p3     = Point(3.0, 4.0, 4.0)
p4     = Point(0.0, 5.0, 5.0)
p5     = Point(12.0, 0.0, 0.0)

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

# TEST CLOUD CLASS

cloud = Cloud()

print(f'Cloud: {cloud}')

if not cloud.is_empty():
    print('Error: cloud should be empty!')

if cloud.extremes() != None:
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

print('Min dist in cloud: {:.3f}'.format(cloud.min_dist()))

print('Test cloud with one point')

cloud1 = Cloud()
p = Point()
cloud1.add_point(p)

print('Min dist in cloud1: {:.3f}'.format(cloud1.min_dist()))
