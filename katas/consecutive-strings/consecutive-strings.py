def longest_consec(strarr, k):
    longest = ''
    for i in range(len(strarr) - k + 1):
        tmp = ''
        for j in range(i, i + k):
            tmp += strarr[j]
        if len(tmp) > len(longest):
            longest = tmp

    return longest
            