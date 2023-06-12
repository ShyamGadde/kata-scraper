def remainder(a, b):
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        pass