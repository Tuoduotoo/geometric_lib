import unittest
from lib.circle import *

class CircleTestCase(unittest.TestCase):

    def test_circle_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_negative_area(self):

        with self.assertRaises(ValueError):
            area(-5)

    def test_circle_little_area(self):
        res = area(5)
        self.assertEqual(res, 5 ** 2 * math.pi)


    def test_circle_large_area(self):
        res = area(700)
        self.assertEqual(res,   math.pi*700 *700)


    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_negative_argument_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_circle_little_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_circle_large_perimeter(self):
        res = perimeter(700)
        self.assertEqual(res, 2 *math.pi * 700)