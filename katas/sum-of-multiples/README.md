# [Sum of Multiples](https://www.codewars.com/kata/57241e0f440cd279b5000829)

- **Completed at:** 2023-07-11T05:02:52.762Z

- **Completed languages:** python

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

## Your Job

  Find the sum of all multiples of `n` below `m` 
  
  
## Keep in Mind

  * `n` and `m` are natural numbers (positive integers)
  * `m` is **excluded** from the multiples
  
  
## Examples

```javascript
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
```
```csharp
Kata.SumMul(2, 9)   => 2 + 4 + 6 + 8 = 20
Kata.SumMul(3, 13)  => 3 + 6 + 9 + 12 = 30
Kata.SumMul(4, 123) => 4 + 8 + 12 + ... = 1860
Kata.SumMul(4, 1)   // throws ArgumentException
Kata.SumMul(0, 20)  // throws ArgumentException
```
```r
sum_mul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sum_mul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sum_mul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sum_mul(4, -7)  ==> "INVALID"
```
```java
Kata.sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
Kata.sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
Kata.sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
Kata.sumMul(4, -7)  // throws IllegalArgumentException
```
```scala
sumMul(2, 9)   // => 2 + 4 + 6 + 8 = Some(20)
sumMul(3, 13)  // => 3 + 6 + 9 + 12 = Some(30)
sumMul(4, 123) // => 4 + 8 + 12 + ... = Some(1860)
sumMul(4, -7)  // => None (m must be greater than 0)
sumMul(-4, 7)  // => None (n must be greater than 0)
sumMul(0, 2)   // => None
sumMul(2, 0)   // => None
```
```cobol
      SumMul(2, 9)   => 2 + 4 + 6 + 8 = 20
      SumMul(3, 13)  => 3 + 6 + 9 + 12 = 30
      SumMul(4, 123) => 4 + 8 + 12 + ... = 1860
      SumMul(4, 1)   => -1
      SumMul(0, 20)  => -1
```
