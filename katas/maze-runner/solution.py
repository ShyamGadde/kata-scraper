def maze_runner(maze, directions):
    current_pos = get_start_pos(maze)
    moves = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }
    
    for direction in directions:
        y, x = current_pos
        y_inc, x_inc = moves[direction]
        new_y, new_x = y + y_inc, x + x_inc
        
        if new_y < 0 or new_x < 0:
            return 'Dead'
        
        try:
            status = maze[new_y][new_x]
            print(status)
        except IndexError:
            return 'Dead'
        
        if status == 1:
            return 'Dead'
        if status == 3:
            return 'Finish'
        
        current_pos = new_y, new_x
    
    return 'Lost'


def get_start_pos(maze):
    n = len(maze)
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                return y, x
    