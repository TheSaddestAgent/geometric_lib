import unittest

from circle import *


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_rad(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_good(self):
        res = area(10)
        self.assertTrue(1 > res - 314 > 0)

    def test_perimeter_good(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)