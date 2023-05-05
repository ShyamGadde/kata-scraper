def util(chunk):
    if not sum(digit ** 3 for digit in map(int, chunk)) % 2:
        return chunk[::-1]
    else:
        return chunk[1:] + chunk[:1]


def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ''
    
    chunks = [strng[i:i + sz] for i in range(0, len(strng), sz)]
    
    if len(chunks[-1]) < sz:
        del chunks[-1]
        
    return ''.join(map(util, chunks))
        
    