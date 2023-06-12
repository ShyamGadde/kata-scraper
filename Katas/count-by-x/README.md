# [Count by X](https://www.codewars.com/kata/5513795bd3fafb56c200049e)

- **Completed at:** 2023-04-01T04:45:12.960Z

- **Completed languages:** javascript

- **Tags:** Arrays, Fundamentals

- **Rank:** 8 kyu

## Description

Create a function with two arguments that will return an array of the first `n` multiples of `x`. 

Assume both the given number and the number of times to count will be positive numbers greater than `0`. 

Return the results as an array or list ( depending on language ).

### Examples

```cpp
countBy(1,10)  should return  {1,2,3,4,5,6,7,8,9,10}
countBy(2,5)  should return {2,4,6,8,10}
```
```java
countBy(1,10)  // should return  {1,2,3,4,5,6,7,8,9,10}
countBy(2,5)  // should return {2,4,6,8,10}
```
```javascript
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
```
```nasm
mov rdi, .memory ; {,,,,,,,,}
mov esi, 1
mov rdx, 10
call cntbyx     ; [RAX] <- {1,2,3,4,5,6,7,8,9,10}

mov rdi, .memory  ; {,,,,}
mov esi 2
mov rdx, 5
call cntbyx     ; [RAX] <- {2,4,6,8,10}
```
```coffeescript
countBy(1,10) == [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) == [2,4,6,8,10]
```
```dart
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
```
```coffeescript
countBy(1,10) == [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) == [2,4,6,8,10]
```
```python
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```ruby
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```crystal
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```
```julia
countby(1,10) === [1,2,3,4,5,6,7,8,9,10]
countby(2,5) === [2,4,6,8,10]
```
```r
count_by(1,10) #should return c(1,2,3,4,5,6,7,8,9,10)
count_by(2,5) #should return c(2,4,6,8,10)
```
```haskell
countBy 1 10 `shouldBe` [1,2,3,4,5,6,7,8,9,10]
countBy 2  5 `shouldBe` [2,4,6,8,10]
```
```lambdacalc
count-by 1 10 -> [1,2,3,4,5,6,7,8,9,10]
count-by 2  5 -> [2,4,6,8,10]
```
```elixir
count_by(1, 10) == [1,2,3,4,5,6,7,8,9,10]
count_by(2, 5) == [2,4,6,8,10]
```
```solidity
countBy(1,10) // should return [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) // should return [2,4,6,8,10]
```
```php
countBy(1,10) // should return [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) // should return [2,4,6,8,10]
```
```groovy
Kata.countBy(1, 10) == [1,2,3,4,5,6,7,8,9,10]
Kata.countBy(2, 5) == [2,4,6,8,10]
```
```racket
(count-by 1 10) ; returns '(1 2 3 4 5 6 7 8 9 10)
(count-by 2 5)  ; returns '(2 4 6 8 10)
```
```rust
count_by(1, 10) // should return vec![1,2,3,4,5,6,7,8,9,10]
count_by(2,5) // should return vec![2,4,6,8,10]
```

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `Scott`  
export `foldl` for your `List` encoding  
~~~