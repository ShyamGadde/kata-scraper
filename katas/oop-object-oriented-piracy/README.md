# [OOP: Object Oriented Piracy ](https://www.codewars.com/kata/54fe05c4762e2e3047000add)

- **Completed at:** 2023-07-01T07:36:42.907Z

- **Completed languages:** python

- **Tags:** Object-oriented Programming, Fundamentals

- **Rank:** 8 kyu

## Description

Ahoy matey!

You are a leader of a small pirate crew. And you have a plan.
With the help of OOP you wish to make a pretty efficient system to identify ships with heavy booty on board!

Unfortunately for you, people weigh a lot these days, so how do you know if a ship is full of gold and not people?

You begin with writing a generic Ship class / struct:
```javascript
function Ship(draft,crew) {
 this.draft = draft;
 this.crew = crew;
}
```
```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
```
```csharp
public class Ship
{
  public int Draft;
  public int Crew;
  
  public Ship(int draft, int crew)
  {
    Draft = draft;
    Crew = crew;
  }
}
```
```rust
struct Ship {
  draft: u32,
  crew: u32,
}
```
```java
public class Ship {
    private final double draft;
    private final int crew;
    
    public Ship(double draft, int crew) {
        this.draft = draft;
        this.crew = crew;
    }
} 
```

Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:

* draft - an estimate of the ship's weight based on how low it is in the water
* crew - the count of crew on board

```javascript
var titanic = new Ship(15, 10);
```
```python
Titanic = Ship(15, 10)
```
```csharp
Ship titanic = new Ship(15, 10);
```
```rust
  let titanic = Ship {
      draft : 15,
      crew : 10,
  };
```
```java
Ship titanic = new Ship(15, 10);
```

## Task
You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.

Each crew member adds `1.5` units to the ship draft. If after removing the weight of the crew, the draft is still more than `20`, then the ship is worth looting. Any ship weighing that much must have a lot of booty!

Add the method
```javascript
isWorthIt
``` 
```python
is_worth_it
``` 
```rust
is_worth_it(&self)
``` 
```csharp
IsWorthIt
```
```java
isWorthIt
```
to decide if the ship is worthy to loot. For example:

```javascript
titanic.isWorthIt() // return false
```
```python
Titanic.is_worth_it()
False
```
```csharp
titanic.IsWorthIt() => false
```
```rust
titanic.is_worth_it() -> false
```
```java
titanic.isWorthIt() == false
```

Good luck and may you find GOOOLD!
