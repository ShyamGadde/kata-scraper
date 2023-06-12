def min_sum(arr):
    arr.sort()
    mid = len(arr) // 2
    return sum(a * b for a, b in zip(arr[:mid], arr[mid:][::-1]))