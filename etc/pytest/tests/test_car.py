import pytest


def test_car_accelerate(my_car):
    my_car.accelerate()
    assert my_car.speed == 55


def test_car_brake(my_car):
    my_car.brake()
    assert my_car.speed == 45


# Apply parameterization: run tests with predefined set of data
speed_data = {45, 50, 55, 100}


@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake_param(speed_brake, my_car):
    my_car.brake()
    assert my_car.speed == speed_brake


@pytest.mark.parametrize("speed_accelerate", speed_data)
def test_car_accelerate_param(speed_accelerate, my_car):
    my_car.accelerate()
    assert my_car.speed == speed_accelerate
