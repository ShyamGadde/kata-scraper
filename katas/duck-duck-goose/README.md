# [Duck Duck Goose](https://www.codewars.com/kata/582e0e592029ea10530009ce)

- **Completed at:** 2023-06-16T02:08:15.332Z

- **Completed languages:** python

- **Tags:** Arrays, Lists, Fundamentals

- **Rank:** 8 kyu

## Description

The objective of [Duck, duck, goose](https://en.wikipedia.org/wiki/Duck,_duck,_goose) is to _walk in a circle_, tapping on each player's head until one is chosen.

----

Task:
~~~if-not:haskell
Given an array of Player objects and a position (first position is 1), return the `name` of the chosen Player.<br>`name` is a property of `Player` objects, e.g `Player.name`
~~~
~~~if:haskell
Given a list of `Player`s and a position (first position is 1), return the `name` of the chosen `Player`.

```haskell
newtype Player = Player {name :: String} deriving (Show, Eq)
```
~~~
----

Example:
~~~if-not:php,haskell
```
duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name
```
~~~
~~~if:php
```php
duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]
```
~~~
~~~if:haskell
```haskell
duckDuckGoose [a, b, c, d] 1 == name a
duckDuckGoose [a, b, c, d] 5 == name a
duckDuckGoose [a, b, c, d] 4 == name d
```
~~~
----

~~~if-not:php
Random input limits:
* `$6 \le \text{Players} \le 50$`
* `$5000 \le \text{Position} \le 50000$`
~~~