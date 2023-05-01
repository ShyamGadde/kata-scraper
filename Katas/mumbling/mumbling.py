def accum(s):
    chars = [*s.lower()]
    for i in range(0, len(chars)):
        chars[i] *= (i + 1)
        chars[i] = chars[i][0].upper() + chars[i][1:]
    return '-'.join(chars)