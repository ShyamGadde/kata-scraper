def delete_nth(lst, max_e):
    counts = {}
    output = []
    for num in lst:
        if counts.setdefault(num, 0) < max_e:
            counts[num] += 1
            output.append(num)
    return output