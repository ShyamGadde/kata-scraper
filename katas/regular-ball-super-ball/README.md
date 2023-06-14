# [Regular Ball Super Ball](https://www.codewars.com/kata/53f0f358b9cb376eca001079)

- **Completed at:** 2023-06-14T09:29:44.987Z

- **Completed languages:** python

- **Tags:** Fundamentals

- **Rank:** 8 kyu

## Description

Create a class `Ball`. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

```javascript
ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
```
```coffeescript
ball1 = new Ball()
ball2 = new Ball("super")
ball1.ballType #=> "regular"
ball2.ballType #=> "super"
```
```ruby
ball1 = Ball.new
ball2 = Ball.new "super"
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```
```python
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```
```scala
ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
```