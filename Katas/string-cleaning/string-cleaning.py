def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join(filter(lambda ch: not ch.isdecimal(), [*s]))