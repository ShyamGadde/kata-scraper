def longest_palindrome(s: str) -> int:
    if len(s) == 0:
        return 0
    
    max_length = 1
    for i in range(len(s)):
        # Check for even length palindrome
        low = i
        high = i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
            low -= 1
            high += 1

        # Check for odd length palindrome
        low = i - 1
        high = i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
            low -= 1
            high += 1

    return max_length