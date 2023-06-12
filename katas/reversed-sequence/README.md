# [Reversed sequence ](https://www.codewars.com/kata/5a00e05cc374cb34d100000d)

- **Completed at:** 2023-03-21T09:19:55.165Z

- **Completed languages:** javascript

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

Build a function that returns an array of integers from n to 1 where ```n>0```.

Example : `n=5` --> `[5,4,3,2,1]`

~~~if:nasm
*NOTE: In NASM, the function signature is* `int *reverse_seq(int n, size_t *size)` *where the first parameter* `n` *is as described above and the second parameter* `size` *is a pointer to an "out" parameter which should be set to the size of the array your function returns (which should be equal to* `n` *if your implementation is correct).*
~~~

~~~if:riscv
RISC-V: The function signature is

```c
void n_to_1(int n, int *arr);
```

Write your result to `arr`. You may assume it is large enough to hold the result. You do not need to return anything.
~~~