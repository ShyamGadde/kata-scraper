def tidyNumber(n):
    digits = str(n)
    for i in range(1, len(digits)):
        if digits[i] < digits[i - 1]:
            return False
    return True
        