def duplicate_encode(word):
    from collections import Counter
    
    word = word.lower()
    counts = Counter(word)
    return ''.join(list(map(lambda ch: '(' if counts[ch] == 1 else ')', word)))