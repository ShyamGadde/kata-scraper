def multiplication_table(size):
    res = []
    for i in range(1, size + 1):
        res.append(
            [j * i for j in range(1, size+1)]
        )
    return res