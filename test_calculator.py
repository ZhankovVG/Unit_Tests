import unittest
import basic_calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(basic_calculator.addition(2, 2), 4)
        self.assertEqual(basic_calculator.addition(-2, 2), 0)
        self.assertEqual(basic_calculator.addition(-2, -2), -4)

    def test_subtraction(self):
        self.assertEqual(basic_calculator.subtraction(2, 2), 0)
        self.assertEqual(basic_calculator.subtraction(-2, 2), -4)
        self.assertEqual(basic_calculator.subtraction(-2, -2), 0)

    def test_multiplication(self):
        self.assertEqual(basic_calculator.multiplication(2, 2), 4)
        self.assertEqual(basic_calculator.multiplication(-2, 2), -4)
        self.assertEqual(basic_calculator.multiplication(-2, -2), 4)

    def test_division(self):
        self.assertEqual(basic_calculator.division(4, 2), 2)
        self.assertEqual(basic_calculator.division(-2, 2), -1)
        self.assertEqual(basic_calculator.division(1, 2), 0.5)


    def test_power(self):
        self.assertEqual(basic_calculator.power(2, 2), 4)
        self.assertEqual(basic_calculator.power(4, 2), 16)
        self.assertEqual(basic_calculator.power(6, 2), 36)

    def test_sqroot(self):
        self.assertEqual(basic_calculator.sqroot(4), 2)
        self.assertEqual(basic_calculator.sqroot(25), 5)
        self.assertEqual(basic_calculator.sqroot(225), 15)



if __name__ == '__main__':
    unittest.main()