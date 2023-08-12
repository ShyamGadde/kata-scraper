def find_slope(points):
    x1, y1, x2, y2 = points
    try:
        return str((y2-y1) // (x2-x1))
    except ZeroDivisionError:
        return 'undefined'