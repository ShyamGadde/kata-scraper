# [Age Range Compatibility Equation](https://www.codewars.com/kata/5803956ddb07c5c74200144e)

- **Completed at:** 2023-08-28T05:40:39.817Z

- **Completed languages:** python

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

Everybody knows the classic ["half your age plus seven"](https://en.wikipedia.org/wiki/Age_disparity_in_sexual_relationships#The_.22half-your-age-plus-seven.22_rule) dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone. 

<!-- Original link is dead. Replaced with archive.org link.
<img src="http://weknowmemes.com/wp-content/uploads/2014/08/age-range-compatibility-equation.jpg" style="width: 400px;"/>
-->
<img src="http://web.archive.org/web/20190206114947if_/http://weknowmemes.com/wp-content/uploads/2014/08/age-range-compatibility-equation.jpg" style="width: 400px;"/>

```minimum age <= your age <= maximum age```

## Task

Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so use this equation instead:
```
min = age - 0.10 * age
max = age + 0.10 * age
```
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). ```Return your answer in the form [min]-[max]```

##Examples:

```
age = 27   =>   20-40
age = 5    =>   4-5
age = 17   =>   15-20
```
