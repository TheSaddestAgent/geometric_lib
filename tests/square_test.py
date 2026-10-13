import unittest

from square import *

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_ok(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_zero_length(self):
        res = perimeter(0)
        self.assertEqual(res, 0)