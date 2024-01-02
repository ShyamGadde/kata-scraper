# [Two Sum](https://www.codewars.com/kata/52c31f8e6605bcc646000082)

- **Completed at:** 2023-03-31T11:33:09.022Z

- **Completed languages:** javascript

- **Tags:** Arrays, Fundamentals, Algorithms

- **Rank:** 6 kyu

## Description

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: `(index1, index2)`.

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

```elixir
two_sum([1, 2, 3], 4) == {0, 2}
```
```lambdacalc
two-sum < 1 2 3 > 4 # returns (0, 2) or (2, 0)
```
```cpp
two_sum({1, 2, 3}, 4); // returns {0, 2} or {2, 0}
```
```go
TwoSum([]int{1, 2, 3}, 4) // returns [2]int{0, 2}
// the go translation has an issue where random tests accept either [2]int{0, 2} or [2]int{2, 0}, but fixed tests and sample tests demand the resulting slice to be sorted!
// untill it's fixed, please sort your result in go.
```
```haskell
twoSum [1, 2, 3] 4 === (0, 2)
```
```javascript
twoSum([1, 2, 3], 4) // returns [0, 2] or [2, 0]
```
```python
two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
```
```rust
two_sum(&[1, 2, 3], 4) // return (0, 2) or (2, 0)
```
```cobol
      TwoSum([1, 2, 3], 4) => result = [1, 3]
```
```scala
twoSum(List(1, 2, 3), 4) // (0, 2) or (2, 0)
```
~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` for your `List` encoding  
export deconstructors `fst, snd` for your `Tuple` encoding  
~~~
