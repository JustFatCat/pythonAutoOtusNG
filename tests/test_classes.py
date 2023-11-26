from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest

@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5, 10, 50, 30),
                          (6, 9, 54, 30)],
                         ids=["set of positive numbers #1", "set of positive numbers #2", "set of positive numbers #3"])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (-5, -10, 50, -30),
                          (0, 0, 0, 0)],
                         ids=["set of negative numbers #1", "set of negative numbers #2", "zero set"])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20),
                          (6, 36, 24)],
                         ids=["set of positive numbers #1", "set of positive numbers #2", "set of positive numbers #3"])
def test_square(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(-4, 16, -20),
                          (-5, 25, 20),
                          (-6, 36, -24)],
                         ids=["set of negative numbers #1", "set of negative numbers #2", "set of negative numbers #3"])
def test_square_negative(side, area, perimeter):
    with pytest.raises(ValueError):
        r = Square(side)
        assert r.name == f"Square {side}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(3, 4, 5, 18, 12),
                          (8, 6, 4, 67.5, 18),
                          (10, 10, 6, 409.5, 26)],
                         ids=["set of positive numbers #1", "set of positive numbers #2", "set of positive numbers #3"])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    tr = Triangle(side_a, side_b, side_c)
    assert tr.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert tr.get_area() == area
    assert tr.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-3, -4, -5, 18, -12),
                          (0, 0, 0, 0, 0),
                          (-10, 10, -6, -409.5, 26)],
                         ids=["set of negative numbers #1", "zero set", "set of negative numbers #2"])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        tr = Triangle(side_a, side_b, side_c)
        assert tr.name == f"Triangle {side_a} and {side_b} and {side_c}"
        assert tr.get_area() == area
        assert tr.get_perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(11, 379.94, 69.08),
                         (7, 153.86, 43.96),
                         (3, 28.26, 18.84)],
                         ids=["set of positive numbers #1", "set of positive numbers #2", "set of positive numbers #3"])
def test_circle(radius, area, perimeter):
    cr = Circle(radius)
    assert cr.name == f"Circle {radius}"
    assert cr.get_area() == area
    assert cr.get_perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-11, -379.94, -69.08),
                          (0, 0, 0),
                          (-3, -28.26, -18.84)],
                         ids=["set of negative numbers #1", "zero set", "set of negative numbers #2"])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        cr = Circle(radius)
        assert cr.name == f"Circle {radius}"
        assert cr.get_area() == area
        assert cr.get_perimeter() == perimeter

def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35

def test_add_area_negative():
    with pytest.raises(AssertionError):
        r = Rectangle(2, 5)
        c = Circle(10)
        assert c.add_area(r) == 15
