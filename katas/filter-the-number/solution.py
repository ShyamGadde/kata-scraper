def filter_string(string):
    return int(''.join(filter(lambda c: c.isdigit(), string)))