def get_even_numbers(arr):
    return list(filter(lambda x: not x & 1, arr))