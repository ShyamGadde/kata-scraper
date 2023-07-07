import re 
def validate_pin(pin):
    return bool(re.fullmatch(r"\d{4}|\d{6}",pin)) 