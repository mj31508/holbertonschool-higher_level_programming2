#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_with_ints(self):
        self.assertEqual(max_integer([1,2,3,4]),4)

    def test_float(self):
        self.assertEqual(max_integer([1,2.0,3,4],2.0)

    def test_large_int(self):
        self.assertTrueEqual(max_integer([54085308],54085308)

    def test_bool(self):
        self.assertEqual(max_integer([True, False, 3, 4], 4)

     def test_list_of_string(self):
        self.assertEqual(max_integer(["Holby"]), "Holby")

    def test_max_string(self):
        self.assertEqual(max_integer("Hakeem"), 'm')

    def test_bool_list(self):
        self.assertEqual(max_integer([True, False, 3, 4]), 4)

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -1, -19, 2]), 2)

    def test)none(self):
        self.assertEqual(max_integer([None]), None)

    @unittest.expectedFailure
    def test_c_list(self):
        self.assertEqual(max_integer(c), NameError)

    @unittest.expectedFailure
    def test_none_at_all(self):
        self.assertEqual(max_integer([None, None, None, None]), TypeError)

    @unittest.expectedFailure
    def test_no_paren(self):
        self.assertEqual(max_integer(None), TypeError)

    @unittest.expectedFailure
    def test_minus(self):
        self.assertEqual(max_integer(-[1, 2, 3, 4]), TypeError)

    @unittest.expectedFailure
    def test_one_digit(self):
        self.assertEqual(max_integer([1]), TypeError)

    @unittest.expectedFailure
    def test_with_No_ints(self):
        self.assertEqual(max_integer([1, None, 3, None]), TypeError)

    @unittest.expectedFailure
    def test_string_in_intlist(self):
        self.assertEqual(max_integer([1, 2, 3, "hi"]), TypeError)

    @unittest.expectedFailure
    def test_string(self):
        self.assertEqual(max_integer(["max", 1,2,3], TypeError)
