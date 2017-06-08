#!/usr/bin/python3
"""
Module to find the max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_isint(self):
        a =  4
        print("test_isint")
        self.assertTrue(max_integer([a, 2]) == 4)

    def test_maxnum(self):
        print("test_maxnum")
        self.assertEqual(max_integer([1, 12, 4]), 12)

    def num_at_end(self):
        print("test num at end")
        self.assertTrue(max_integer([1,2,3,4]) == 4)

    def test_float(self):
        print("test_float")
        self.assertEqual(max_integer([4.0]), 4.0)

    def first_num(self):
        self.assertEqual(max_integer([4,3,2,1]))

    def mid_max(self):
        self.assertEqual(max_integer([1,2,4,3]), 4)

    def neg_number(self):
        self.assertTrue(max_integer([1,2,-3,4]), 4)

    def only_neg(self):
        self.assertTrue(max_integer([-1,-2,-3,-4]))

    def one_num(self):
        self.assertTrue(max_integer([4]))

    def is_empty(self):
        self.assertTrue(max_integer([]))

if __name__ == '__main__':
        unittest.main()
