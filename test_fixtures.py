import pytest
from add import add

@pytest.fixture
def data():
	return {'python':1,'java':2}


def test_programing_language(data):
	# login(user_data['dipesh']) == True
	assert data['python']==1

# unittest
from unittest import TestCase

calss TestCaseFirst(TestCase):
	def test_method_1(self):
		self.assert add(5)==20
