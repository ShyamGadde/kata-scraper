# [Odd-Even String Sort](https://www.codewars.com/kata/580755730b5a77650500010c)

- **Completed at:** 2023-07-26T00:36:50.990Z

- **Completed languages:** python

- **Tags:** Strings, Fundamentals, Sorting

- **Rank:** 7 kyu

## Description

Given a string `s`, your task is to return another string such that even-indexed and odd-indexed characters of `s` are grouped and the groups are space-separated. Even-indexed group comes as first, followed by a space, and then by the odd-indexed part.

### Examples

```text
input:    "CodeWars" => "CdWr oeas"
           ||||||||      |||| ||||
indices:   01234567      0246 1357
```

Even indices 0, 2, 4, 6, so we have `"CdWr"` as the first group.  
Odd indices are 1, 3, 5, 7, so the second group is `"oeas"`.  
And the final string to return is `"Cdwr oeas"`.