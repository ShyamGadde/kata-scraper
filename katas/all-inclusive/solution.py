def contain_all_rots(strng, arr):
    arr = set(arr)
    rots = {strng[i:] + strng[:i] for i in range(len(strng))}
    return rots <= arr