def solve(arr):
    return [sum(ord(ch) - 65 == i for i, ch in enumerate(strng.upper())) for strng in arr]