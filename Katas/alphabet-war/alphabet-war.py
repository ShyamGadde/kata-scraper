left_side = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1
}

right_side = {
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1
}

def alphabet_war(fight):
    left_side_score = right_side_score = 0
    
    for letter in fight:
        if letter in left_side:
            left_side_score += left_side[letter]
        elif letter in right_side:
            right_side_score += right_side[letter]
    
    if left_side_score == right_side_score:
        return "Let's fight again!"
    else:
        return f'{"Right" if right_side_score > left_side_score else "Left"} side wins!'