def largest_pair_sum(numbers): 
    numbers.sort()
    return sum(numbers[-2:])
    