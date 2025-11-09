import pytest
from shapes import Sphere, Cube, Cylinder, Rectangle


# Simple tests for the shapes
# As tests used single examples I have followed this approach without using parameterized tests for this part of the assignment


########################## SPHERE TESTS ##########################
sphere = Sphere(5)


def test_sphere_calculate_area() -> None:
    # Formula: 4 * π * r^2
    assert sphere.calculate_area() == pytest.approx(314.159, abs=0.001)


def test_sphere_calculate_volume() -> None:
    # Formula: (4 / 3) * π * r^3
    assert sphere.calculate_volume() == pytest.approx(523.598, abs=0.001)


########################## CYLINDER TESTS ##########################
cylinder = Cylinder(5, 10)


def test_cylinder_calculate_area() -> None:
    # Formula: 2 * π * r * (r + h)
    assert cylinder.calculate_area() == pytest.approx(471.239, abs=0.001)


def test_cylinder_calculate_volume() -> None:
    # Formula: π * r^2 * h
    assert cylinder.calculate_volume() == pytest.approx(785.398, abs=0.001)


########################## RECTANGLE TESTS ##########################
rectangle = Rectangle(5, 10)


def test_rectangle_calculate_area() -> None:
    # Formula: length * width
    assert rectangle.calculate_area() == pytest.approx(50.0, abs=0.001)


def test_rectangle_calculate_volume() -> None:
    # Formula: 0 (2D shape has no volume)
    assert rectangle.calculate_volume() == pytest.approx(0.0, abs=0.001)


########################## CUBE TESTS ##########################
cube = Cube(5)


def test_cube_calculate_area() -> None:
    # Formula: 6 * side^2
    assert cube.calculate_area() == pytest.approx(150.0, abs=0.001)


def test_cube_calculate_volume() -> None:
    # Formula: side^3
    assert cube.calculate_volume() == pytest.approx(125.0, abs=0.001)
