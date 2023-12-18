import unittest

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_Area_Zero(self):
        self.assertRaises(ValueError, area, 0, 12)

    def test_rectangle_area(self):
        self.assertEquals(area(4, 7), 28)

    def test_rectangle_negative_area(self):
        self.assertRaises(ValueError, area, -123, -12)

    def test_rectangle_perimeter(self):
        self.assertEquals(perimeter(23, 20), 86)

    def test_rectangle_perimeter_zero(self):
        self.assertRaises(ValueError, perimeter, 0, 3)

    def test_rectangle_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -4, 234)

def area(a, b):
    '''Принимает числа a и b, возвращает их произведение'''
    return a * b

def perimeter(a, b):
    '''Принимает числа a и b, возвращает удвоенную сумму этих чисел'''
    return 2*(a + b)
