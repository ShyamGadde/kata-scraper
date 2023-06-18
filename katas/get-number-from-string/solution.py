def get_number_from_string(string):
    return int(''.join(filter(str.isdigit, string)))