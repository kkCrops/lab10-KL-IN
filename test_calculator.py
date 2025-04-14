# Repository Link: https://github.com/kkCrops/lab10-KL-IN
# Partner 1: Karen Liang
# Partner 2: Izzy Nunag

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(10,3), 13)
        self.assertEqual(add(-1, -1), -2)
        self.assertNotEqual(add(0, 5), 0)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(-5, -7), 2)
        self.assertNotEqual(sub(0, 5), 5)
    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(6, 0), 0)
        self.assertAlmostEqual(mul(-6, -1), 6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertAlmostEqual(div(2, 7), 3.5)
        self.assertEqual(div(2.1, -6.3), -3)
    ##########################

    # Partner 2
    def test_divide_by_zero(self):# 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(47, 103823), 3)
        self.assertNotEqual(logarithm(10, 10), 10)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self):
        # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
<<<<<<< HEAD
=======
        with self.assertRaises(ValueError):
            logarithm(0, 6)

>>>>>>> ff0617b57bdb02117ef59cf3200e9354015301d6

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(4, 0), 4)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()