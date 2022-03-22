import unittest
import pytest

from add_numbers import (
        add,
    )

class AddNumbersTests(unittest.TestCase):

    @pytest.mark.task(taskno=1)
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
    
    # This can be handled to ignore chars but not a requirement
    def test_returns_sum_of_two_chars_and_numbers(self):
        self.assertEqual(add("a1, b2"), 0)
    
    def test_returns_sum_of_numbers_with_spaces_in_string(self):
        self.assertEqual(add("1, 2"), 3)

    def test_return_zero_for_string_with_spaces(self):
        self.assertEqual(add("    "), 0)

    def test_return_zero_for_string_with_spaces_commas(self):
        self.assertEqual(add("    , "), 0)

    # Initial code should be able to handle multiple numbers
    @pytest.mark.task(taskno=2)
    def test_returns_sum_of_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4,5,6"), 21)

    def test_returns_sum_of_multiple_numbers_with_spaces(self):
        self.assertEqual(add("2, 5, 3, 32, 6, "), 48)

    @pytest.mark.task(taskno=3)
    def test_returns_sum_of_multiple_numbers_with_newlines_in_string(self):
        self.assertEqual(add("1\n2,3"), 6)
    
    def test_returns_sum_of_multiple_numbers_with_arbitrary_newlines_commas_in_string(self):
        self.assertEqual(add("1\n\n2\n\n,\n\n,\n\n4"), 7)
        self.assertEqual(add(",,,,,\n\n\n\n,2,n\n\n\n,,,,,4"), 6)
        self.assertEqual(add("     ,,,,\n\n\n\n\n,2       \n,\n,\n,     12,,,,,\n4"), 18)

    # Tests such that a delimiter is specified in the string
    @pytest.mark.task(taskno=4)
    def test_returns_sum_of_multiple_numbers_with_delimiter_semicolon(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_returns_sum_of_multiple_numbers_with_delimiter_hash(self):
        self.assertEqual(add("//#\n1#2"), 3)
    
    def test_returns_sum_of_multiple_numbers_with_delimiter_asterisk(self):
        self.assertEqual(add("//*\n1*2"), 3)
    
    # My code would not function well if the space is a delimiter, what if it is
    def test_returns_sum_of_multiple_numbers_with_delimiter_space(self):
        self.assertEqual(add("// \n1 2"), 3)

    def test_returns_sum_of_multiple_numbers_with_delimiter_tab(self):
        self.assertEqual(add("//\t\n1\t2"), 3)

    def test_returns_sum_of_multiple_numbers_with_delimiter_newline(self):
        self.assertEqual(add("//\n\n1\n2"), 3)

if __name__ == "__main__":
    unittest.main()
