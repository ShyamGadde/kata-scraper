def max_sequence(arr):
    best_sum = current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum