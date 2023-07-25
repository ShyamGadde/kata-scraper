import math


def convert_fracts(lst):
    if not lst:
        return []
    
    lcm = math.lcm(*list(zip(*lst))[1])
    return list(map(lambda item: [item[0] * (lcm // item[1]), lcm] , lst))
    