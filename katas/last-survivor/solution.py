def last_survivor(letters, coords): 
    contestants = [*letters]
    
    for coord in coords:
        del contestants[coord]
    
    return contestants[0]