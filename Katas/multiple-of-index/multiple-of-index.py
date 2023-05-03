def multiple_of_index(arr):
    return [item[1] for item in enumerate(arr[1:], start=1) if not item[1] % item[0]]