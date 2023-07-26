from itertools import accumulate


def array_leaders(numbers):
    suffix_arr = list(accumulate(numbers[::-1], initial=0))[::-1]
    
    res = []
    
    for i, n in enumerate(numbers):
        if n > suffix_arr[i + 1]:
            res.append(n)
            
    return res