def solve(s):
    if sum(ch.isupper() for ch in s) > len(s) // 2:
        return s.upper()
    return s.lower()