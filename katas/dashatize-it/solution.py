def dashatize(n):
    if not isinstance(n, int):
        return "None"
    
    num_str = str(abs(n))
    
    for i in range(1, 10, 2):
        num_str = num_str.replace(str(i), f'-{i}-')
    
    return num_str.strip('-').replace('--', '-')