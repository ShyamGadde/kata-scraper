def stray(arr):
    from collections import Counter
    for key,value in Counter(arr).items():
        if value == 1:
            return key