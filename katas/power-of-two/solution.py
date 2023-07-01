def power_of_two(x):
    if x < 1:
        return False
    return not (x & (x - 1))