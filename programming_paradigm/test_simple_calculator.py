import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalsulator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3,5),8)
        self.assertEqual(self.calc.add(-3, 5), 2)
        self.assertEqual(self.calc.add(5,-3), 2)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertNotEqual(self.calc.add(3,5), "35")
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(3, 0), 3)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,5), 20)
        self.assertEqual(self.calc.multiply(0,4), 0)
        self.assertEqual(self.calc.multiply(4, 0), 0)
        self.assertNotEqual(self.calc.multiply(4, 3), "444")
    def test_division(self):
        self.assertIsNone(self.calc.divide(3, 0))
        self.assertEqual(self.calc.divide(0,3),0)
        self.assertEqual(self.calc.divide(3,2), 1.5)

    