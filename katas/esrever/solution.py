def reverse(lst):
    print(lst)
    empty_list = list()
    
    for i in range(1, len(lst) + 1):
        empty_list.append(lst[-i])
    
    return empty_list
    