import re

def abbreviate(s):
    def replace_word(match):
        word = match.group(0)
        return word[0] + str(len(word) - 2) + word[-1]

    pattern = r'[a-zA-Z]{4,}'
    return re.sub(pattern, replace_word, s)