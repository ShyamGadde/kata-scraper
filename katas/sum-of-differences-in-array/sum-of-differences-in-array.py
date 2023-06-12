def sum_of_differences(arr):
    diff_sum = 0
    arr.sort(reverse=True)
    for i in range(1, len(arr)):
        diff_sum += arr[i - 1] - arr[i]
    return diff_sum
        
    