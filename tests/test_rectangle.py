import pytest
import source.shapes as shapes



def test_rectangle(rectangle):

    assert rectangle.area() == 10 * 20


def test_perimeter(rectangle):

    assert rectangle.perimeter() == (10*2)+(20*2)


def test_not_equal(rectangle, rectangle2):
    assert rectangle != rectangle2