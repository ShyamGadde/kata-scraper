# [Linked Lists - Length & Count](https://www.codewars.com/kata/55beec7dd347078289000021)

- **Completed at:** 2023-08-18T04:54:05.335Z

- **Completed languages:** python

- **Tags:** Linked Lists, Data Structures, Fundamentals

- **Rank:** 6 kyu

## Description

Linked Lists - Length & Count

Implement `length` to count the number of nodes in a linked list.<br>
```javascript
length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
```
```csharp
Node.Length(nullptr) => 0
Node.Length(1 -> 2 -> 3 -> nullptr) => 3
```
```cpp
Length(null) => 0
Length(1 -> 2 -> 3 -> null) => 3
```
```cobol
      NodeListLength(null) => 0
      NodeListLength(1 -> 2 -> 3 -> null) => 3
```
```lambdacalc
length nil # 0
length (1 -> 2 -> 3 -> nil) # 3
```
~~~if-not:csharp,lambdacalc
Implement Count() to count the occurrences of an integer in a linked list.
~~~
~~~if:csharp
Implement Count() to count the occurrences of a that satisfy a condition provided by a predicate which takes in a node's Data value.
~~~
~~~if:lambdacalc
Implement `count` to count the occurrences of an element in a linked list. A function `eq` is preloaded for you to make comparisons, which will return `True = \ a _ . a` or `False = \ _ b . b`.
~~~

```javascript
count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
```
```csharp
Node.Count(null, value => value == 1) => 0
Node.Count(1 -> 3 -> 5 -> 6, value => value % 2 != 0) => 3
```
```cpp
Count(null, 1) => 0
Count(1 -> 2 -> 3 -> nullptr, 1) => 1
Count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> nullptr, 2) => 4
```
```cobol
      NodeListCount(null, 1) => 0
      NodeListCount(1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
```
```lambdacalc
count nil 1 # 0
count (1 -> 2 -> 3 -> nil) 1 # 1
count (1 -> 1 -> 2 -> 1 -> 2) 2 # 2
```

I've decided to bundle these two functions within the same Kata since they are both very similar.

~~~if:lambdacalc
### Lambda Calculus Notes

In the LC translations of this series, we use the Scott encoding of a linked list. In this encoding, a list is a function which accepts two arguments. If the list is `nil` then it returns the first argument (the default case), otherwise it will pass its data and tail to the second argument. In practice this looks like this:
```lambdacalc
my-list (default-case) (\ data next . result)
```
For this kata, `nil` is defined for you in `Preloaded` like this:
```lambdacalc
nil = \ n _ . n
```

In addition, we also use the [Scott encoding](https://github.com/codewars/lambda-calculus/wiki/encodings-guide#scott-numerals) of numbers.
~~~

The `push()`/`Push()` and `buildOneTwoThree()`/`BuildOneTwoThree()` functions do not need to be redefined.

Related Kata in order of expected completion (increasing difficulty):<br>
 <a href="http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree">Linked Lists - Push & BuildOneTwoThree</a><br>
 <a href="http://www.codewars.com/kata/linked-lists-length-and-count">Linked Lists - Length & Count</a><br>
 <a href="http://www.codewars.com/kata/linked-lists-get-nth-node">Linked Lists - Get Nth Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-insert-nth-node">Linked Lists - Insert Nth Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-insert">Linked Lists - Sorted Insert</a><br>
<a href="http://www.codewars.com/kata/linked-lists-insert-sort">Linked Lists - Insert Sort</a><br>
<a href="http://www.codewars.com/kata/linked-lists-append">Linked Lists - Append</a><br>
<a href="http://www.codewars.com/kata/linked-lists-remove-duplicates">Linked Lists - Remove Duplicates</a><br>
<a href="http://www.codewars.com/kata/linked-lists-move-node">Linked Lists - Move Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-move-node-in-place">Linked Lists - Move Node In-place</a><br>
<a href="http://www.codewars.com/kata/linked-lists-alternating-split">Linked Lists - Alternating Split</a><br>
<a href="http://www.codewars.com/kata/linked-lists-front-back-split">Linked Lists - Front Back Split</a><br>
<a href="http://www.codewars.com/kata/linked-lists-shuffle-merge">Linked Lists - Shuffle Merge</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-merge">Linked Lists - Sorted Merge</a><br>
<a href="http://www.codewars.com/kata/linked-lists-merge-sort">Linked Lists - Merge Sort</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-intersect">Linked Lists - Sorted Intersect</a><br>
<a href="http://www.codewars.com/kata/linked-lists-iterative-reverse">Linked Lists - Iterative Reverse</a><br>
<a href="http://www.codewars.com/kata/linked-lists-recursive-reverse">Linked Lists - Recursive Reverse</a><br>

Inspired by Stanford Professor Nick Parlante's excellent [Linked List teachings.](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)