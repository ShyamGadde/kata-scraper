def men_from_boys(arr):
    men = set(filter(lambda x: not x & 1, arr))
    boys = set(arr) - men
    return sorted(men) + sorted(boys, reverse=True)