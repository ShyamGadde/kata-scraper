# [Delete occurrences of an element if it occurs more than n times](https://www.codewars.com/kata/554ca54ffa7d91b236000023)

- **Completed at:** 2023-05-10T12:06:01.630Z

- **Completed languages:** python

- **Tags:** Lists, Fundamentals

- **Rank:** 6 kyu

## Description

## Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.  
He tells them that he will only sit for the session if they show the same motif at most `N` times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to `N` times, without changing the order?

## Task

Given a list and a number, create a new list that contains each number of `list` at most `N` times, without reordering.  
For example if the input number is `2`, and the input list is `[1,2,3,1,2,1,2,3]`, you take `[1,2,3,1,2]`, drop the next `[1,2]` since this would lead to `1` and `2` being in the result `3` times, and then take `3`, which leads to `[1,2,3,1,2,3]`.  
With list `[20,37,20,21]` and number `1`, the result would be `[20,37,21]`.  

~~~if:nasm
## NASM notes

Write the output numbers into the `out` parameter, and return its length.

The input array will contain only integers between 1 and 50 inclusive. Use it to your advantage.
~~~

~~~if:c
For C:
* Assign the return array length to the pointer parameter `*szout`.
* Do not mutate the input array.
~~~

~~~if:lambdacalc
## Encodings

purity: `LetRec`  
numEncoding: `Church`  
export constructors `nil, cons` and deconstructor `foldr` for your `List` encoding  
~~~