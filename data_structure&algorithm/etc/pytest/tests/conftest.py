import pytest
from ..Car import Car


@pytest.fixture
def my_car():
    return Car(50)
