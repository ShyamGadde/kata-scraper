# [Keep Hydrated!](https://www.codewars.com/kata/582cb0224e56e068d800003c)

- **Completed at:** 2023-04-16T04:03:45.600Z

- **Completed languages:** javascript

- **Tags:** Algorithms, Mathematics, Fundamentals

- **Rank:** 8 kyu

## Description

Nathan loves cycling. 

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:
~~~if-not:sql
```
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
```
~~~
~~~if:sql
```
hours = 3 ----> liters = 1

hours = 6.7---> liters = 3

hours = 11.8--> liters = 5
```

Input data is available from the table `cycling`, which has 2 columns: `id` and `hours`. For each row, you have to return 3 columns: `id`, `hours` and `liters` (not litres, it's a difference from the kata description)
~~~