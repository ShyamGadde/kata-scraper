# [Maximum  subarray sum](https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c)

- **Completed at:** 2023-05-11T13:07:57.817Z

- **Completed languages:** python

- **Tags:** Algorithms, Lists, Dynamic Programming, Fundamentals, Performance

- **Rank:** 5 kyu

## Description

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

```haskell
maxSequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]
-- should be 6: [4, -1, 2, 1]
```
```javascript
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]
```
```python
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
```
```clojure
(max-sequence [-2, 1, -3, 4, -1, 2, 1, -5, 4])
;; should be 6: [4, -1, 2, 1]
```
```java
Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
// should be 6: {4, -1, 2, 1}
```
```scala
Max.sequence(Array(-2, 1, -3, 4, -1, 2, 1, -5, 4));
// should be 6: Array(4, -1, 2, 1)
```
```kotlin
maxSequence(listOf(-2, 1, -3, 4, -1, 2, 1, -5, 4));
// should be 6: listOf(4, -1, 2, 1)
```
```c
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4}, 9)
// should return 6, from sub-array: {4, -1, 2, 1}
```
```cpp
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4});
//should be 6: {4, -1, 2, 1}
```
```rust
max_sequence(&[-2, 1, -3, 4, -1, 2, 1, -5, 4]);
//should be 6: [4, -1, 2, 1]
```
```cobol
       maxSequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      * should be 6: [4, -1, 2, 1]
```

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
