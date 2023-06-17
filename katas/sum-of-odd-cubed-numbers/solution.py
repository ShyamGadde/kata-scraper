def cube_odd(arr):
    if all(type(x) == int for x in arr):
        return sum(filter(lambda x: x % 2, map(lambda x: x ** 3, arr)))