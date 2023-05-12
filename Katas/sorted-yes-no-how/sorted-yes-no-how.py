def is_sorted_and_how(arr):
    if arr[0] < arr[-1]:  # ascending
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return 'no'
        return 'yes, ascending'
    else:  # descending
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                return 'no'
        return 'yes, descending'