def find_uniq(arr):
    from collections import Counter
    return Counter(arr).most_common()[-1][0]
    