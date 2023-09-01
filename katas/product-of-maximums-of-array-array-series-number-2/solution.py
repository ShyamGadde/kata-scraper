import math

def max_product(lst, n):
    return math.prod(sorted(lst, reverse=True)[:n])