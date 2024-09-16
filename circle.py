import unittest
import math

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_Area_Zero(self):
        self.assertRaises(ValueError, area, 0)

    def test_rectangle_area(self):
        self.assertEquals(area(4), 16*math.pi)

    def test_rectangle_negative_area(self):
        self.assertRaises(ValueError, area, -123)

    def test_rectangle_perimeter(self):
        self.assertEquals(perimeter(23), 2*math.pi*23)

    def test_rectangle_perimeter_zero(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_rectangle_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -41)

def area(r):
    '''Принимает число r, возвращает квадртат числа r умноженное на Pi'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает удвоенное произведение Pi на r'''
    return 2 * math.pi * r
