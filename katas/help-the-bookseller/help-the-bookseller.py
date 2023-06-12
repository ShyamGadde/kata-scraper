def stock_list(list_of_art, list_of_cat):
    if list_of_art and list_of_cat:
        return ' - '.join([f'({c} : {sum(int(item[1]) for item in map(str.split, list_of_art) if item[0][0] == c)})' 
                       for c in list_of_cat])
    return ''