def decipher_this(s):
    words = s.split()
    
    for i, word in enumerate(words):
        first = ''
        rem = ''
        
        for j, ch in enumerate(word):
            if ch.isdigit():
                first += ch
            else:
                rem = word[j:]
                break
        
        if len(rem) > 1:
            rem = rem[-1] + rem[1:-1] + rem[0]
        words[i] = f'{chr(int(first))}{rem}'
        
    return ' '.join(words)