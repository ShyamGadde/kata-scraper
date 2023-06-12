operations = {
    "add":      lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide":   lambda x, y: x / y,
}

def arithmetic(a, b, operator):
    return operations[operator](a, b)