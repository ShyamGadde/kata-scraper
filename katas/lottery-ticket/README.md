# [Lottery Ticket](https://www.codewars.com/kata/57f625992f4d53c24200070e)

- **Completed at:** 2023-08-26T04:21:01.246Z

- **Completed languages:** python

- **Tags:** Fundamentals, Strings, Arrays

- **Rank:** 6 kyu

## Description

Time to win the lottery!

Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot. 

Example ticket:

```javascript
[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
```
```cpp
{ { "ABC", 65 }, { "HGR", 74 }, { "BYHT", 74 } }
```
```c
{ { "ABC", 65 }, { "HGR", 74 }, { "BYHT", 74 } }
```
```julia
[ [ "ABC", 65 ], [ "HGR", 74 ], [ "BYHT", 74 ] ]
```
```rust
[ ( "ABC", 65 ), ( "HGR", 74 ), ( "BYHT", 74 ) ]
```

To do this, you must first count the 'mini-wins' on your ticket.  Each subarray has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length.


