def is_triangle(a, b, c):
    return True if ((a+b>c) and (a+c>b) and (b+c>a)) else False