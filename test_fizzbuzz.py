import unittest
from main import fizzbuzz
class TestFizzBuzz(unittest.TestCase):

    def test_1_should_return_1(self):
        result = fizzbuzz(1)
        expected = "1"
        self.assertEqual(result, expected)