import unittest

class SquareTestCase(unittest.TestCase):
    def test_square_Area_Zero(self):
        self.assertRaises(ValueError, area, 0)

    def test_square_area(self):
        self.assertEquals(area(4), 16)

    def test_square_negative_area(self):
        self.assertRaises(ValueError, area, -123)

    def test_square_perimeter(self):
        self.assertEquals(perimeter(23), 92)

    def test_square_perimeter_zero(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_square_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -4)

def area(a):
    '''Принимает число a, возвращает квадрат этого числа'''
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает произведение этого числа на 4'''
    return 4 * a
