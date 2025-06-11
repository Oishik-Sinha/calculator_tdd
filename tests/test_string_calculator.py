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

    def test_negative_value_raises_exception(self):
        with self.assertRaises(ValueError) as cm:
            add("1,-2,3,-5")
        self.assertIn("negative numbers not allowed -2,-5", str(cm.exception))

    def test_negative_value_raises_exception_test2(self):
        with self.assertRaises(ValueError) as cm:
            add("1,-2,3,-5\n-7")
        self.assertIn("negative numbers not allowed -2,-5,-7", str(cm.exception))

if __name__ == "__main__":
    unittest.main()