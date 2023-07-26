def automorphic(n):
    sq = str(n * n)
    digits = len(str(n))
    
    return 'Automorphic' if n == int(sq[-digits:]) else 'Not!!'
    