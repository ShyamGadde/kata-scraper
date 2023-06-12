def unique_in_order(iterable):
    if not iterable:
        return []

    unique = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i-1]:
            unique.append(iterable[i])
    return unique