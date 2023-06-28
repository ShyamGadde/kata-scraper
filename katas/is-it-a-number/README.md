# [Is it a number?](https://www.codewars.com/kata/57126304cdbf63c6770012bd)

- **Completed at:** 2023-06-27T23:39:49.671Z

- **Completed languages:** python

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

```javascript
isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
```

should return false:

```javascript
isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")
```