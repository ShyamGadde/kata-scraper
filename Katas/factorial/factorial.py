import operator
from functools import reduce

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
    return reduce(operator.mul, range(1, n + 1), 1)