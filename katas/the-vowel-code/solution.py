def encode(st):
    table = str.maketrans('aeiou', '12345')
    return st.translate(table)
    
def decode(st):
    table = str.maketrans('12345', 'aeiou')
    return st.translate(table)