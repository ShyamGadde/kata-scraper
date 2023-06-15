def race(v1, v2, lead):
    if v1 >= v2:
        return
    
    v1_fps = v1 / 3600
    v2_fps = v2 / 3600
    
    time_seconds = round(lead / (v2_fps - v1_fps), 2)
    
    hours = time_seconds // 3600
    minutes = (time_seconds % 3600) // 60
    seconds = int(time_seconds % 60)
    
    return [hours, minutes, seconds]
        