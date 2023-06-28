def isDigit(string):
    try:
        float(string)        
    except ValueError:
        return False
    else:
        return True