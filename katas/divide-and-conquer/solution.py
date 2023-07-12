def div_con(x):
    res = 0
    for elem in x:
        if type(elem) == int: res += elem
        else: res -= int(elem)
    return res