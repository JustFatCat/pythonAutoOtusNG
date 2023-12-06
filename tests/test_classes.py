from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest

@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5.6, 11.3, 63.28, 33.8)],
                         ids=["set of positive integers", "set of positive floats"])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(-4, -6),
                          (0, 0)],
                         ids=["set of negative integers", "zero set"])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)

@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 16, 16),
                          (5.7, 32.49, 22.8)],
                         ids=["set of positive integers", "set of positive floats"])
def test_square(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize("side",
                         [-4,
                          0],
                         ids=["negative integer", "zero"])
def test_square_negative(side):
    with pytest.raises(ValueError):
        r = Square(side)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(3, 4, 5, 18, 12),
                          (8.2, 4.2, 5.2, 43.71839999999994, 17.599999999999998)],
                         ids=["set of positive integers", "set of positive floats"])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    tr = Triangle(side_a, side_b, side_c)
    assert tr.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert tr.get_area() == area
    assert tr.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(-3, -4, -5),
                          (0, 0, 0)],
                         ids=["set of negative integers", "zero set"])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        tr = Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(11, 379.94, 69.08),
                         (7.8, 191.0376, 48.984)],
                         ids=["set of positive integers", "set of positive floats"])
def test_circle(radius, area, perimeter):
    cr = Circle(radius)
    assert cr.name == f"Circle {radius}"
    assert cr.get_area() == area
    assert cr.get_perimeter() == perimeter

@pytest.mark.parametrize("radius",
                         [-11,
                          0],
                         ids=["negative integer", "zero"])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        cr = Circle(radius)

def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35

def test_add_area_negative():
    with pytest.raises(AssertionError):
        r = Rectangle(2, 5)
        c = Circle(10)
        assert c.add_area(r) == 15
