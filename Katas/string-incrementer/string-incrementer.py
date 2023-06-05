import re

def increment_string(strng):
    match = re.search(r'^(.*?)(\d+)$', strng)
    if match:
        preceding_part = match.group(1)
        number_part = match.group(2)
        number_len = len(number_part)

        return f'{preceding_part}{int(number_part) + 1:0{number_len}}'
    
    return f'{strng}1'