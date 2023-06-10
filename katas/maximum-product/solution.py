def adjacent_element_product(array):
    res = float('-inf')
    for i in range(1, len(array)):
        res = max(res, array[i - 1] * array[i])
    return res