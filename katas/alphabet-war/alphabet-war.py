alphabets = {
    'w': -4,
    'p': -3,
    'b': -2,
    's': -1,
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1
}

def alphabet_war(fight):
    score = 0
    for letter in fight:
        score += alphabets.get(letter, 0)
    
    if score == 0:
        return "Let's fight again!"
    return f"{'Right' if score > 0 else 'Left'} side wins!"