def isPP(n):
    m = 2
    while True:
        k = 2
        while m ** k <= n:
            if m ** k == n:
                return [m, k]
            k += 1
        m += 1
        if m ** 2 > n:
            break