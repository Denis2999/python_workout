import math


class Circle():
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return self.radius ** 2 * 3.14159265

    def perimeter(self):
        return 2 * self.radius * 3.14159265


if __name__ == '__main__':
    radius = float(input())
    c1 = Circle(radius)
    print(c1.getArea())

    dims = input().split(" ")
    width = float(dims[0])
    height = float(dims[1])
    r1 = Rectangle(width, height)
    print(r1.getArea())

    radius = float(input())
    c2 = Circle(radius)
    print(c2.getArea())

    width = float(input())
    s1 = Square(width)
    print(s1.getArea())

    dims = input().split(" ")
    width = float(dims[0])
    height = float(dims[1])
    r2 = Rectangle(width, height)
    print(r2.getArea())
