def bingo(ticket,win):
    return "Winner!" if sum(any(ord(ch) == num for ch in string) for string, num in ticket) >= win else "Loser!"