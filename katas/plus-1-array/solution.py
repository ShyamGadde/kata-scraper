def up_array(arr):
    if arr and all(0 <= x < 10 for x in arr):
        res = list(map(int, str(int(''.join(map(str, arr))) + 1)))
        return [0] * (len(arr) - len(res)) + res