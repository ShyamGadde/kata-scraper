import re


def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    
    fresh_fruits = []
    
    for fruit in bag_of_fruits:
        match = re.search(r'([A-Z][a-z]+)', fruit)
        if match:
            fresh_fruits.append(match.group(1).lower())
        else:
            fresh_fruits.append(fruit)
            
    return fresh_fruits