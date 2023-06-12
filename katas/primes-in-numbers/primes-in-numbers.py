def prime_factors(n):
    from collections import Counter
    return ''.join([f'({k}**{v})' if v > 1 else f'({k})' for k, v in Counter(pfactors(n)).items()])
        
    
    
def pfactors(n):
    p = 2
    while(n > 1):
        if n % p == 0:
            yield p
            n /= p
        else:
            p += 1