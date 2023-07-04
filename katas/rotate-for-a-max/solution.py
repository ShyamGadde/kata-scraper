def max_rot(n):
    options, digits = [n], str(n)
    
    for i in range(len(digits)):
        digits = digits[:i] + digits[i + 1:] + digits[i]
        options.append(int(digits))
    
    return max(options)