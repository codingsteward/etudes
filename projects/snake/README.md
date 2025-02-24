# Snake

## Game requirements

1. Represent a snake game
2. Snake can move NSEW
3. Eat food, spawn a new one

## Data structures

1. Snake head: point
2. snake body: array
3. food: point
4. board: matrix

## core functions

move(direction) -> None // state update internally
1. Get new coordinate for snake head
2. Check if collision with wall or body
3. Check if eat food
4. Loop

isCollision() -> bool
1. checks boundaries for wall
2. check if coordinates in snake body, use a dictionary or set of tuples

isEatFood() -> bool
1. check if new coordinate equals food coordinate
2. if true, do not pop tail coordinate

updateRemaining state
1. remove end of tail coordinate
2. 



