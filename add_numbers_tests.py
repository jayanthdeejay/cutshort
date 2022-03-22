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

    # couple of edge edge cases
    def test_returns_sum_of_two_chars(self):
        self.assertEqual(add("a, b"), 0)
    
    def test_returns_sum_of_no_chars(self):
        self.assertEqual(add(","), 0)
    
    # This can be handled to ignore chars but not the requirement
    def test_returns_sum_of_two_chars_and_numbers(self):
        self.assertEqual(add("a1, b2"), 0)
    
    def test_returns_sum_of_numbers_with_spaces_in_string(self):
        self.assertEqual(add("1, 2"), 3)


if __name__ == "__main__":
    unittest.main()
