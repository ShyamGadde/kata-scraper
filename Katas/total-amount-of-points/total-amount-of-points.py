def points(games):
 return sum(get_points(scores) for scores in games)
    
def get_points(scores):
    x, y = scores.split(':')
    if x > y:
        return 3
    if x < y:
        return 0
    return 1