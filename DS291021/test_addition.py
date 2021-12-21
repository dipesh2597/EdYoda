import pytest
from add_function import add

def test_case_recharge1():
	assert add(3,2)==5

def test_case_recharge2():
	assert add(5,5) == 5

def test_case_recharge3():
	assert add(3,2) == 5
	assert add(5,1) == 5


def print_hello():
	print("hello")
	assert add(3,2)==5

def test_case_flight_booking1():
	assert add(5,5)==10

@pytest.mark.recharge
def test_recharge_1():
	assert add(3,2) == 1


@pytest.mark.recharge
def test_recharge_2():
	assert add(3,2) == 5

@pytest.mark.flights
def test_flights_1():
	assert add(3,2) == 1


@pytest.mark.flights
def test_flights_2():
	assert add(3,2) == 5
