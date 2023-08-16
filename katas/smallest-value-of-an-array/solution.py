def find_smallest(numbers,to_return):
    smallest = min(enumerate(numbers), key=lambda x: x[1])
    return smallest[0] if to_return == "index" else smallest[1]