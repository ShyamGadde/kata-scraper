def encrypt_this(text):
    words = text.split()
    
    for i in range(len(words)):
        if len(words[i]) > 2:
            words[i] = words[i][0] + words[i][-1] + words[i][2:-1] + words[i][1]
        words[i] = f'{ord(words[i][0])}{words[i][1:]}'
    
    return ' '.join(words)