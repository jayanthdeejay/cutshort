import unittest
from add_numbers import (
        add,
    )

class AddNumbersTests(unittest.TestCase):
    def test_returns_zero_for_empty_string(self):
        self.assertEqual(add(""), 0)
    
    def test_returns_sum_of_one_number(self):
        self.assertEqual(add("12"), 12)

    def test_returns_sum_of_two_numbers(self):
        self.assertEqual(add("1,2"), 3)