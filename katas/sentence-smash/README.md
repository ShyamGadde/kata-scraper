# [Sentence Smash](https://www.codewars.com/kata/53dc23c68a0c93699800041d)

- **Completed at:** 2023-05-01T08:51:55.133Z

- **Completed languages:** python

- **Tags:** Strings, Arrays, Fundamentals

- **Rank:** 8 kyu

## Description

# Sentence Smash

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. **Be careful, there shouldn't be a space at the beginning or the end of the sentence!**

## Example

```
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
```

```ruby
words = ['hello', 'world', 'this', 'is', 'great']
smash(words) # returns "hello world this is great"
```
```haskell
smash ["hello", "world", "this", "is", "great"] `shouldBe` "hello world this is great"
```
```elixir
words = ["hello", "world", "this", "is", "great"]
smash(words) # returns "hello world this is great"
```


## Assumptions

* You can assume that you are only given words.
* You cannot assume the size of the array.
* You can assume that you do get an array.

## What We're Testing

We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.

## Disclaimer

This is for beginners so we want to test basic loops and string manipulation. Advanced users should easily be able to do this in one line.
