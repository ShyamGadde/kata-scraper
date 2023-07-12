def pairs(ar):
    count = 0
    
    for i in range(1, len(ar), 2):
        x, y = ar[i - 1], ar[i]
        
        if abs(x - y) == 1:
            count += 1
    
    return count