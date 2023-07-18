# [Maze Runner](https://www.codewars.com/kata/58663693b359c4a6560001d6)

- **Completed at:** 2023-07-18T05:09:44.011Z

- **Completed languages:** python

- **Tags:** Arrays, Fundamentals

- **Rank:** 6 kyu

## Description

# Introduction

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!
</pre>

# Task

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return <span style="color:#A1A85E">Finish</span>. If you hit any walls or go outside the maze border, you should return <span style="color:#A1A85E">Dead</span>. If you find yourself still in the maze after using all the moves, you should return <span style="color:#A1A85E">Lost</span>.
</pre>

The Maze array will look like
```
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
```
..with the following key

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point
</pre>
```lua
  direction = {"N","N","N","N","N","E","E","E","E","E"} == "Finish"
```
```c
  directions = "NNNNNEEEEE" == "Finish" // (directions passed as a string)
```
```ruby
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
```python
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
```javascript
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
```php
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
```csharp
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
```haskell
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```
# Rules

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
1. The Maze array will always be square i.e. <span style="color:#A1A85E">N x N</span> but its size and content will alter from test to test.

2. The <span style="color:#A1A85E">start</span> and <span style="color:#A1A85E">finish</span> positions will change for the final tests.

3. The directions array will always be in upper case and will be in the format of <span style="color:#A1A85E">N = North, E = East, W = West and S = South</span>.

4. If you reach the end point before all your moves have gone, you should return <span style="color:#A1A85E">Finish</span>.

5. If you hit any walls or go outside the maze border, you should return <span style="color:#A1A85E">Dead</span>.

6. If you find yourself still in the maze after using all the moves, you should return <span style="color:#A1A85E">Lost</span>.
</pre>

Good luck, and stay safe!

# Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58663693b359c4a6560001d6" target="_blank">Maze Runner</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58693bbfd7da144164000d05" target="_blank">Scooby Doo Puzzle</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/7KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134" target="_blank">Driving License</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/586c0909c1923fdb89002031" target="_blank">Connect 4</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f" target="_blank">Vending Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027" target="_blank">Snakes and Ladders</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58a848258a6909dd35000003" target="_blank">Mastermind</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051" target="_blank">Guess Who?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Am I safe to drive?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Mexican Wave</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e" target="_blank">Pigs in a Pen</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/590300eb378a9282ba000095" target="_blank">Hungry Hippos</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/5904be220881cb68be00007d" target="_blank">Plenty of Fish in the Pond</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/590adadea658017d90000039" target="_blank">Fruit Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/> <a href="https://www.codewars.com/kata/591eab1d192fe0435e000014" target="_blank">Car Park Escape</a></span>