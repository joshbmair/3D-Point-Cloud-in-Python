# Point Cloud
## Introduction
This is the Python version of the Point Cloud assignment I had to do in one of my first computer science classes. The original assignment was in Java and fit only 2-dimensional points; however, I chose to rewrite this in Python and make points 3-dimensional as a challenge to myself.


## What is a point, and what is a cloud?
A point is an object with an x, y, and z value like on a 3D Euclidian plane, and a cloud is a collection of points. Easy enough to understand.

## How to use
This repository is now formatted like a library where you can import a point without a cloud. You can also import a cloud without a point, but a cloud without any points is useless.

To import a point and cloud, use the following lines of code:
```
from PointCloud import Point
from PointCloud import Cloud
```
From there you can use the various methods under the point and cloud classes.