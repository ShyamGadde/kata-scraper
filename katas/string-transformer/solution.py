import re


def string_transformer(s):
    return "".join(re.findall(r"\S+|\s+", s.swapcase())[::-1])