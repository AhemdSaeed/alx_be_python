import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 10), 5)

    # ---------- Subtraction Tests ----------
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 8), -5)

    def test_subtraction_with_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    # ---------- Multiplication Tests ----------
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiplication_with_negatives(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -4), 8)

    # ---------- Division Tests ----------
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(3, 2), 1.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_with_negatives(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

if __name__ == "__main__":
    unittest.main()
