#!/usr/bin/python3
"""
Unittest for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20]), -5)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -10, 3]), 5)
        self.assertEqual(max_integer([0, -5, 10]), 10)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)

    def test_max_at_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 3, 10, 5]), 10)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 3, 5]), 5)

    def test_zero(self):
        """Test with zeros"""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.2]), 3.2)
        self.assertEqual(max_integer([1.1, 1.2, 1.15]), 1.2)


if __name__ == '__main__':
    unittest.main()
