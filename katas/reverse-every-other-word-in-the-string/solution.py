import re


def reverse_alternate(s):
    words = re.split(r'\s+', s.strip())
    
    words = [words[i][::-1] if i & 1 else words[i] for i in range(len(words))]
            
    return ' '.join(words)