def name_value(my_list):
    return [sum(ord(ch) - 96 for ch in string if ch.islower()) * pos for pos, string in enumerate(my_list, start=1)]