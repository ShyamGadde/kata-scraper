def show_sequence(n):
    if n == 0:
        return "0=0"
    if n < 0:
        return f"{n}<0"
    
    seq = list(range(n + 1))
    return f"{'+'.join(map(str, seq))} = {sum(seq)}"