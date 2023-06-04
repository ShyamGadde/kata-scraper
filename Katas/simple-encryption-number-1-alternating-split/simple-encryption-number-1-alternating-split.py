def decrypt(encrypted_text, n):
    if not encrypted_text:
        return encrypted_text

    chars = [*encrypted_text]
    length = len(chars)

    for _ in range(n):
        half_length = length // 2
        first_half = chars[half_length:]
        second_half = chars[:half_length]
        chars = [char for pair in zip(first_half, second_half) for char in pair]
        if length % 2:
            chars.append(first_half[-1])

    return ''.join(chars)



def encrypt(text, n):
    if not text:
        return text
    
    chars = [*text]
    for _ in range(n):
        chars = [char for i, char in enumerate(chars) if i % 2] + [char for i, char in enumerate(chars) if not i % 2]
    
    return ''.join(chars)