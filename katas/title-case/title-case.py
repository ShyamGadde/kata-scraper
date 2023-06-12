def title_case(title, minor_words=''):
    if not title:
        return ''
    ignore_words = set(minor_words.lower().split())
    res = [word.capitalize() if word not in ignore_words else word for word in title.lower().split()]
    res[0] = res[0].capitalize()
    return ' '.join(res)
    