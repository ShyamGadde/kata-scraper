def gps(s, x):
    if len(x) < 2:
        return 0
    
    delta_distances = [y - x for x, y in zip(x[:-1], x[1:])]
    speed_per_hour = [(3600 * delta_distance) / s for delta_distance in delta_distances]
    return int(max(speed_per_hour))