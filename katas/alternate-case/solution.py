def alternate_case(s):
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in s)