import math


def divisors(n):
    divs = [1]
    for i in range(2, int(n ** .5) + 1):
        if not n % i:
            divs.extend([i, n // i])
    divs.extend([n])
    return set(divs)


def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        squared_divs_sum = sum(map(lambda x: x ** 2, divisors(i)))
        if squared_divs_sum == math.isqrt(squared_divs_sum) ** 2:
            res.append([i, squared_divs_sum])
    return res