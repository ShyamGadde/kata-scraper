def get_middle(s):
    s_len = len(s)
    if s_len % 2:  # odd
        return s[s_len // 2]
    else:
        return s[s_len // 2 - 1:s_len // 2 + 1]
        