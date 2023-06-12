def nearest_sq(n):
    sqrt = n ** .5 // 1
    if sqrt ** 2 == n:
        return n
    elif n - sqrt ** 2 < (sqrt + 1) ** 2 - n:
        return sqrt ** 2
    return (sqrt + 1) ** 2
    