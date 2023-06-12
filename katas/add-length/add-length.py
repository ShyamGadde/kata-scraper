def add_length(str_):
    return list(map(lambda s: f"{s} {len(s)}", str_.split(" ")))