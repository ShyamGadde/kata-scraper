# [Sum without highest and lowest number](https://www.codewars.com/kata/576b93db1129fcf2200001e6)

- **Completed at:** 2023-03-31T11:20:35.140Z

- **Completed languages:** javascript

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

## Task

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

## Example

    { 6, 2, 1, 8, 10 } => 16
    { 1, 1, 11, 2, 3 } => 6

## Input validation

If an empty value ( `null`, `None`, `Nothing`, `nil` etc. ) is given instead of an array, or the given array is an empty list or a list with only `1` element, return `0`.