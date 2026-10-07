import unittest

from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_equal_lengths(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_dif_lenghts(self):
        res = perimeter(10, 3)
        self.assertEqual(res, 26)