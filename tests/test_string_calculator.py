import unittest
# from calculator.string_calculator import add
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers_separated_by_comma(self):
        self.assertEqual(add("1,5"), 6)
    
    def test_more_than_one_numbers_separated_by_comma(self):
        self.assertEqual(add("1,5,2"), 8)

    def test_handle_any_amount_of_numbers(self):
        self.assertEqual(add("1,5,2,9,3,1"), 21)
    
    def test_allow_new_line_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)
    
    def test_support_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

if __name__ == "__main__":
    unittest.main()