import pytest
import source.shapes as shapes


@pytest.mark.parametrize('side_length, expected_area', [(5, 25), (3, 9), (10,100)])
def test_multiple_squares(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area