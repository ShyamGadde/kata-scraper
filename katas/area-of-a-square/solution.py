import math


def square_area(A):
    side_length = A * 2 / math.pi
    return round(side_length ** 2, 2)