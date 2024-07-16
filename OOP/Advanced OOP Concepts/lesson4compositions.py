# handling compositions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f"Point ({self.x}, {self.y})"
class Shape:
    def __init__(self, points):
        self.points = points
    def __repr__(self) -> str:
        point_str = ','.join(repr(point) for point in self.points) #using join
        return f"Points:({point_str})"

triangle = Shape([Point(0,0), Point(1,2), Point(5,5)])
square = Shape([Point(0,0), Point(0,10), Point(0,10), Point(10,10)])
print(triangle.points)
print(square.points)
print(square)