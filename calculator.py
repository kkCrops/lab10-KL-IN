import math

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError
    else:
        return math.log(b,a)

def exp(a,b):
    return a**b

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return math.pow(a, b)




