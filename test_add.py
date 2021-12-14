from add import add
import pytest

def test_case_1():
	assert add(15)==20
	assert add(25)>=40
	assert add(5)==20
	assert add(-5)==10

def test_case_2():
	assert add(15)==30

def login(username,password):
	#logic
	return True

def test_case_3():
	assert login('dipesh','dipesh') == True

def test_always_pass():
	assert True

@pytest.mark.edyoda
def test_edyoda_1():
	assert add(1)==6

@pytest.mark.edyoda
def test_edyoda_2():
	assert add(2)==5
