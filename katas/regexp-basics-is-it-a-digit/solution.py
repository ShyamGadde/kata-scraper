import re


def is_digit(n):
    pattern = r'^[0-9]$'
    match = re.search(pattern, n.replace('\n', ' '))
    return match is not None