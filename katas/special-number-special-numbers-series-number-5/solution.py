def special_number(number):
    if all(digit in '012345' for digit in str(number)):
        return "Special!!"
    else:
        return "NOT!!"