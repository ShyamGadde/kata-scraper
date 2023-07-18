# [All Inclusive?](https://www.codewars.com/kata/5700c9acc1555755be00027e)

- **Completed at:** 2023-07-18T04:38:49.771Z

- **Completed languages:** python

- **Tags:** Fundamentals, Strings

- **Rank:** 7 kyu

## Description

Input: 

- a string `strng`
- an array of strings `arr`

Output of function `contain_all_rots(strng, arr) (or containAllRots or contain-all-rots)`:

- a boolean `true` if all rotations of `strng` are included in `arr`
- `false` otherwise

#### Examples:
```
contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
```

#### Note: 
Though not correct in a mathematical sense

- we will consider that there are no rotations of `strng == ""`
- and for any array `arr`: `contain_all_rots("", arr) --> true`

Ref: <https://en.wikipedia.org/wiki/String_(computer_science)#Rotations>

```if:shell
## Bash:
For bash the array is replaced by a string (see "RUN sample tests"). 
```