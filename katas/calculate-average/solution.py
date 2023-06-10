def find_average(numbers):
    try:
        return sum(numbers)/len(numbers)
    except ZeroDivisionError:
        return 0