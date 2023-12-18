import unittest

class TriangleTestCase(unittest.TestCase):
    def test_triangle_Area_Zero(self):
        self.assertRaises(ValueError, area, 0, 3)

    def test_triangle_area(self):
        res = area(4, 12)
        self.assertEquals(res, 24)

    def test_triangle_negative_area(self):
        self.assertRaises(ValueError, area, -1, 4)

    def test_triangle_perimeter(self):
        res = perimeter(12, 11, 10)
        self.assertEquals(res, 33)

    def test_triangle_perimeter_nonexistent(self):
        self.assertRaises(ValueError, perimeter, 31, 1, 1)

    def test_triangle_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, -23, 43)

def area(a, h):
    '''Принимает числа a и b, возвращает произведение этих чисел, деленное на 2'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает числа a, b, c, возвращает их сумму'''
    return a + b + c
