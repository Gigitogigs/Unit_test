import unittest
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-5, 3), -2)
        self.assertEqual(self.calculator.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-5, 3), -8)
        self.assertEqual(self.calculator.subtract(-5, -3), -2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(5, 3), 15)
        self.assertEqual(self.calculator.multiply(-5, 3), -15)
        self.assertEqual(self.calculator.multiply(-5, -3), 15)
        self.assertEqual(self.calculator.multiply(0, 3), 0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(6, -3), -2)
        self.assertEqual(self.calculator.divide(0, 3), 0)
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
