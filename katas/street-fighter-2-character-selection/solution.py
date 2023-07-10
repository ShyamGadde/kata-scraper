def street_fighter_selection(fighters, initial_position, moves):
    rows, cols = len(fighters), len(fighters[0])
    row, col = initial_position
    
    characters = []
    
    for move in moves:
        if move == 'up':
            row = max(row - 1, 0)
            characters.append(fighters[row][col])
        elif move == 'down':
            row = min(row + 1, rows - 1)
            characters.append(fighters[row][col])
        elif move == 'left':
            col = (col - 1) % cols
            characters.append(fighters[row][col])
        else:
            col = (col + 1) % cols
            characters.append(fighters[row][col])

    return characters