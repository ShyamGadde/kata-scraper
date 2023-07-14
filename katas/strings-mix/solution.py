from collections import Counter


def mix(s1, s2):
    s1_counter = Counter(filter(str.islower, s1))
    s2_counter = Counter(filter(str.islower, s2))
    
    keys = set(s1_counter) | set(s2_counter)
    
    res = []
    for key in keys:
        s1_count, s2_count = s1_counter[key], s2_counter[key]
        
        if s1_count < 2 and s2_count < 2:
            continue
        if s1_count == s2_count:
            res.append(f'=:{key * s1_count}')
        elif s1_count > s2_count:
            res.append(f'1:{key * s1_count}')
        else:
            res.append(f'2:{key * s2_count}')
    
    return '/'.join(sorted(res, key=lambda x: (-len(x), x)))