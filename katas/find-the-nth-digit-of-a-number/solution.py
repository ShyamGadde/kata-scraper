def find_digit(num, nth):
    if nth <1: return -1
    try:
        return int(str(abs(num))[-nth])
    except IndexError:
        return 0