def capitalize(s):
    chars = [*s]
    res = [[], []]
    for i in range(len(chars)):
        if i % 2:
            res[0].append(chars[i])
            res[1].append(chars[i].upper())
        else:
            res[0].append(chars[i].upper())
            res[1].append(chars[i])
    return list(map(''.join, res))