def sum_pairs(ints, s):
    hash_set = set()
    for num in ints:
        if s - num in hash_set:
            return [s - num, num]
        else:
            hash_set.add(num)