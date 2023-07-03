from functools import reduce
from operator import mul

def number_to_pwr(number, p): 
    return reduce(mul, [number]*p, 1)