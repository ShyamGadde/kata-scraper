def warn_the_sheep(queue):
    if queue[-1] == 'wolf': return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {len(queue) - 1 - queue.index("wolf")}! You are about to be eaten by a wolf!'