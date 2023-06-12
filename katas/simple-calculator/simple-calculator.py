def calculator(x,y,op):
    if op not in ['+', '-', '*', '/']:
        return 'unknown value'
    if type(x) != int or type(y) != int:
        return 'unknown value'
    return eval(f'{x} {op} {y}')