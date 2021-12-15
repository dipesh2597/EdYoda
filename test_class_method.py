# unittest
from unittest import TestCase
from add import add

class TestCaseFirst(TestCase):
	def test_method_1(self):
		self.assertEqual(add(5),20)
