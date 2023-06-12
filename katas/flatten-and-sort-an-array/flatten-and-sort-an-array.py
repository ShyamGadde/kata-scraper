def flatten_and_sort(array):
    flat_arr = []
    for l in array:
        flat_arr += l
    return sorted(flat_arr)