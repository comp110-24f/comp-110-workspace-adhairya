__author__ = "730744596"

from CQs.cq09.point import Point

point = Point(1.0, 2.0)
point.scale_by(2)
print(f"({point.x}, {point.y})")

point = Point(1.0, 2.0)
new_point = point.scale(2)
print(f"({point.x}, {point.y})")
print(f"({new_point.x}, {new_point.y})")
