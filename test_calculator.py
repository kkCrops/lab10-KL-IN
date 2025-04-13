# Repository Link: https://github.com/kkCrops/lab10-KL-IN
# Partner 1: Karen Liang
# Partner 2: Izzy Nunag

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(6, 0), 0)
        self.assertAlmostEqual(mul(-6, -1), 6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(0, 6), ZeroDivisionError)
        self.assertEqual(div(2.1, -6.3), -3)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 6)


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