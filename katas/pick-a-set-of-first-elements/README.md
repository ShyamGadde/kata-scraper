# [pick a set of first elements](https://www.codewars.com/kata/572b77262bedd351e9000076)

- **Completed at:** 2023-06-27T23:44:03.475Z

- **Completed languages:** python

- **Tags:** Arrays, Fundamentals

- **Rank:** 8 kyu

## Description

Write a function to get the first element(s) of a sequence. Passing a parameter `n` (default=`1`) will return the first `n` element(s) of the sequence. 

If `n` == `0` return an empty sequence `[]`

### Examples

```javascript
var arr = ['a', 'b', 'c', 'd', 'e'];
first(arr) //=> ['a'];
first(arr, 2) //=> ['a', 'b']
first(arr, 3) //=> ['a', 'b', 'c'];
first(arr, 0) //=> [];
```

```csharp
var arr = new object[] { 'a', 'b', 'c', 'd', 'e' };
Kata.TakeFirstElements(arr); //=> new object[] { 'a' }
Kata.TakeFirstElements(arr, 2);// => new object[] { 'a', 'b' }
Kata.TakeFirstElements(arr, 3); //=> new object[] { 'a', 'b', 'c' }
Kata.TakeFirstElements(arr, 0); //=> new object[] { }
```

```python
arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
```
