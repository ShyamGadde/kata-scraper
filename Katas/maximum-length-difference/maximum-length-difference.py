def mxdiflg(a1, a2):
    if a1 and a2:
        max_a1 = len(max(a1, key=len))
        min_a1 = len(min(a1, key=len))
        
        max_a2 = len(max(a2, key=len))
        min_a2 = len(min(a2, key=len))
        
        return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
    return -1