def meeting(s):
    names = [c.upper().split(':') for c in s.split(';')]
    names.sort(key=lambda name: (name[1], name[0]))
    return ''.join(f'({lname}, {fname})' for fname, lname in names)
    