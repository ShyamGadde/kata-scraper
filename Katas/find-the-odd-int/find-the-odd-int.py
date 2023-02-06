def find_it(seq):
    # Create a dictionary to store the counts of each element
    counts = {}
    # Iterate through the sequence and update the count of each element
    for e in seq:
        counts[e] = counts.get(e, 0) + 1
    # Return the first element with odd number of appearences
    for e in counts:
        if counts[e] % 2:
            return e
    