# [Replace With Alphabet Position](https://www.codewars.com/kata/546f922b54af40e1e90001da)

- **Completed at:** 2023-03-20T01:52:32.427Z

- **Completed languages:** javascript

- **Tags:** Strings, Fundamentals

- **Rank:** 6 kyu

## Description

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

## Example

~~~if-not:nasm
```
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
```
~~~
~~~if:nasm
```nasm
text:  db  "The sunset sets at twelve o' clock.",0h0

main:
    mov rdi, text
    call alphabet_position
```
Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )
~~~
