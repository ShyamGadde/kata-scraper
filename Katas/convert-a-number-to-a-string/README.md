# [Convert a Number to a String!](https://www.codewars.com/kata/5265326f5fda8eb1160004c8)

- **Completed at:** 2023-02-06T07:34:47.315Z

- **Completed languages:** javascript

- **Tags:** Strings, Fundamentals

- **Rank:** 8 kyu

## Description

We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

```if:c
In C, return a dynamically allocated string that will be freed by the test suite.
```

#### Examples (input --> output):

```
123  --> "123"
999  --> "999"
-100 --> "-100"
```

~~~if:riscv
RISC-V: The function signature is:

```c
void number_to_string(int n, char *out);
```

Convert the input number `n` to a string, and write the result to `out`. You may assume `out` is large enough to hold the result. You do not need to return anything.
~~~