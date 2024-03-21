import pytest
import source.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def rectangle2():
    return shapes.Rectangle(5, 6)


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")
