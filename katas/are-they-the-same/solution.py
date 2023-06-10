def comp(a1, a2):
    from collections import Counter

    if a1 is None or a2 is None:
        return False
    
    return Counter(map(lambda x: x * x, a1)) == Counter(a2)
 