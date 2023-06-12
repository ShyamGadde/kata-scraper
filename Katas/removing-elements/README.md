# [Removing Elements](https://www.codewars.com/kata/5769b3802ae6f8e4890009d2)

- **Completed at:** 2023-04-10T06:20:21.311Z

- **Completed languages:** javascript

- **Tags:** Lists, Arrays, Fundamentals

- **Rank:** 8 kyu

## Description

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

### Example:

```if-not:c
`["Keep", "Remove", "Keep", "Remove", "Keep", ...]` --> `["Keep", "Keep", "Keep", ...]`
```

```if:c
~~~c
size_t length = 5;
remove_every_other(&length, {1, 2, 3, 4, 5});
// -->  {1, 3, 5}
~~~
```

None of the arrays will be empty, so you don't have to worry about that!