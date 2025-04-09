import math

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def exp(a,b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)





