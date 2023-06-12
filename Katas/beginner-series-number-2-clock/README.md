# [Beginner Series #2 Clock](https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a)

- **Completed at:** 2023-04-11T04:10:47.950Z

- **Completed languages:** javascript

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

Clock shows `h` hours, `m` minutes and `s` seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

## Example:

```
h = 0
m = 1
s = 1

result = 61000
```

Input constraints:

* `0 <= h <= 23`
* `0 <= m <= 59`
* `0 <= s <= 59`

~~~if:riscv
RISC-V: The function signature is:

```c
int past(int h, int m, int s);
```
~~~
