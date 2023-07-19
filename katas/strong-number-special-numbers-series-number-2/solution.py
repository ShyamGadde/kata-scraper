from math import factorial

def strong_num(number):
    return 'STRONG!!!!' if sum(map(factorial, map(int, str(number)))) == number else 'Not Strong !!'
    