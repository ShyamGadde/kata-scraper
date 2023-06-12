def is_prime(num):
    import math

    if num <= 1:
        return False
    return (
        all(num % i for i in range(3, math.floor(math.sqrt(num)) + 1, 2))
        if num % 2
        else num == 2
    )