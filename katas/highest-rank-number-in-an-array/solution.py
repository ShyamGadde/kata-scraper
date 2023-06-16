def highest_rank(arr):
    from collections import Counter
    
    return sorted(Counter(arr).items(), key=lambda x: (x[1], x[0]))[-1][0]