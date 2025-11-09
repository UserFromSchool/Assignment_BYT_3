import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_volume(self) -> float:
        pass


class Sphere(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return 4 * math.pi * math.pow(self.radius, 2)

    def calculate_volume(self) -> float:
        return (4.0 / 3.0) * math.pi * math.pow(self.radius, 3)


class Cylinder(Shape):
    def __init__(self, radius: float, height: float) -> None:
        self.radius = radius
        self.height = height

    def calculate_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def calculate_volume(self) -> float:
        return math.pi * math.pow(self.radius, 2) * self.height


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_volume(self) -> float:
        return 0.0


class Cube(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def calculate_area(self) -> float:
        return 6 * math.pow(self.side, 2)

    def calculate_volume(self) -> float:
        return math.pow(self.side, 3)


if __name__ == "__main__":
    sphere = Sphere(5)
    print("Sphere:")
    print(f"Area: {sphere.calculate_area():.3f}")
    print(f"Volume: {sphere.calculate_volume():.3f}")
    print()

    cylinder = Cylinder(3, 7)
    print("Cylinder:")
    print(f"Area: {cylinder.calculate_area():.3f}")
    print(f"Volume: {cylinder.calculate_volume():.3f}")
    print()

    rectangle = Rectangle(4, 8)
    print("Rectangle:")
    print(f"Area: {rectangle.calculate_area():.3f}")
    print(f"Volume: {rectangle.calculate_volume():.3f}")
    print()

    cube = Cube(4)
    print("Cube:")
    print(f"Area: {cube.calculate_area():.3f}")
    print(f"Volume: {cube.calculate_volume():.3f}")
