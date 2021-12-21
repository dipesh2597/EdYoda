import pytest
# from login import login
from add_function import add
@pytest.fixture
def data():
	return {'python':1,'java':2}


def test_programing_language(data):
	assert data['python']==2


# @pytest.fixture
# def login_data():
# 	retrun {'dipesh':'dipesh_pass','edyoda':'edyoda','unacademy':'unacademy_pass'}


# def test_login(login_data):
# 	for username in login_data:
# 		assert login(username,login_data[username]) == True

# @test_programing_language
# def print():
# 	return True

# unittest
from unittest import TestCase

class TestCaseFirst(TestCase):
	def test_method_1(self):
		self.assertEqual(add(5,2),10)                      #assert add(5)==20
