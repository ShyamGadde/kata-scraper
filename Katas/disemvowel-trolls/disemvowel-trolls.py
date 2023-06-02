def disemvowel(string_):
    import re
    return re.sub(r'[aeiou]', '', string_, flags=re.IGNORECASE)