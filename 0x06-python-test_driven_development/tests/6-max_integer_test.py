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

    def test_multi_num(self):
        a = 50
        self.assertEqual(max_integer([a,a,a,a]), a)

    def test_unsorted_num(self):
        self.assertEqual(max_integer([1,4,2,2]), 4)

    def test_maxnum(self):
        print("test_maxnum")
        self.assertEqual(max_integer([1, 12, 4]), 12)

    def test_num_at_end(self):
        a = 4
        print("test num at end")
        self.assertEqual(max_integer([1,2,3,a]), a)

    def test_float(self):
        print("test_float")
        self.assertEqual(max_integer([4.0]), 4.0)

    def test_first_num(self):
        self.assertEqual(max_integer([4,3,2,1]), 4)

    def test_mid_max(self):
        self.assertEqual(max_integer([1,2,4,3]), 4)

    def test_neg_number(self):
        self.assertTrue(max_integer([1,2,-3,4]), 4)

    def test_only_neg(self):
        self.assertTrue(max_integer([-1,-2,-3,-4]))

    def test_one_num(self):
        self.assertTrue(max_integer([4]))

    def test_is_empty(self):
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
        unittest.main()
