# [Is the string uppercase?](https://www.codewars.com/kata/56cd44e1aa4ac7879200010b)

- **Completed at:** 2023-05-11T00:16:02.398Z

- **Completed languages:** python

- **Tags:** Fundamentals, Strings

- **Rank:** 8 kyu

## Description

# Is the string uppercase?

## Task

Create a method to see whether the string is ALL CAPS.

### Examples (input -> output)

```
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
```


In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

~~~if:riscv
RISC-V: The function signature is

```c
bool is_uppercase(const char *);
```
~~~