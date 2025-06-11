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

if __name__ == "__main__":
    unittest.main()