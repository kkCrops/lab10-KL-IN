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
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self):# 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)
            div(0, -10)
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(47, 103823), 3)
        self.assertNotEqual(logarithm(10, 10), 10)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
            logarithm(1, 10)
            logarithm(-5, 5)
        # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()