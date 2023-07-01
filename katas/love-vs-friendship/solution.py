def words_to_marks(s):
    return sum(ord(ch)-96 for ch in s)