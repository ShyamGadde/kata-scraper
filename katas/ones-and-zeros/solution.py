def binary_array_to_number(arr):
    dec = 0
    
    for bit in arr:
        dec = (dec << 1) | bit
        
    return dec