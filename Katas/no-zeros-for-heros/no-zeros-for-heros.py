def no_boring_zeros(num):
    while num % 10 == 0 and num != 0:
        num //= 10
    return num