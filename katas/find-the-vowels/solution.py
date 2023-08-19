def vowel_indices(word):
 return [
        index
        for index, ch in enumerate(word, start=1)
        if ch.lower() in "aeiouy"
    ]