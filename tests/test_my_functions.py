import pytest
import  source.my_functions as my_functions
import time


def test_add():
    result = my_functions.add(1,4)
    assert result == 5


def test_divide():
    result = my_functions.divide(10,2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(1,0)


def test_add_strings():
    result = my_functions.add("Hello ","World")
    assert result == "Hello World"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10,2)
    assert result == 5

@pytest.mark.skip(reason="feature is currently not implemented")
def test_multiply():
    time.sleep(2)


@pytest.mark.xfail(reason="feature is currently not working")
def test_divide_by_zero_fail():
    my_functions.divide(2,0)