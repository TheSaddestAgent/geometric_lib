import unittest

from triangle import *

class RectangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_length(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_ok(self):
        res = area(10, 6)
        self.assertEqual(res, 30)

    def test_perimeter_equal_lengths(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_345(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)