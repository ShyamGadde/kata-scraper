def calc(x):
    total1 = ''.join(map(str, map(ord, x)))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))