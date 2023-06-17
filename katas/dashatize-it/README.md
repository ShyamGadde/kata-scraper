# [Dashatize it](https://www.codewars.com/kata/58223370aef9fc03fd000071)

- **Completed at:** 2023-06-17T04:33:30.816Z

- **Completed languages:** python

- **Tags:** Strings, Arrays, Regular Expressions, Fundamentals

- **Rank:** 6 kyu

## Description

Given a variable `n`,

If `n` is an integer,
Return a string with dash``` '-' ```marks before and after each odd integer,  but do not begin or end the string with a dash mark. If `n` is negative, then the negative sign should be removed.

```if:python
If `n` is not an integer, return the string `"None"`.
```
```if:ruby
If `n` is not an integer, return the string `"nil"`.
```
```if:coffeescript,javascript,typescript
If `n` is not an integer, return the string `"NaN"`.
```
```if-not:python,ruby,coffeescript,javascript,typescript
If `n` is not an integer, return an empty value.
```

Ex:
```javascript
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```coffeescript
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```crystal
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```ruby
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```rust
dashatize(274) -> "2-7-4"
dashatize(6815) -> "68-1-5"
```
