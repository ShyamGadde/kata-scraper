def to_nato(words):
    return ' '.join(NATO.get(ch, ch) for ch in words.upper() if not ch.isspace())