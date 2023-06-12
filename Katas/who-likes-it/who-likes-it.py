def likes(names):
    likes = len(names)
    
    if not likes:
        return "no one likes this"
    if likes == 1:
        return f"{names[0]} likes this"
    if likes == 2:
        return f"{names[0]} and {names[1]} like this"
    if likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {likes - 2} others like this"
        
        