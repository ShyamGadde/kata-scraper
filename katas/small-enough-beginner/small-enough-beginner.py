def small_enough(array, limit):
    return all(item <= limit for item in array)