# Snakes game in terminal


## Rendering using curses module

## Game logic in python

## Components
1. Game engine runs the game loop, on each tick, fetch input, move snake, update state, render new state
2. render component takes in current state, render it


SnakeBoard
1. handles the board logic, and rendering window using curse module
2. provides method to interact with the board
3. any state changes will update the board and refresh the window

SnakeEngine
1. handles game loop, has access to game board and game state
2. how does game board knows game state??


Snake contains the persistent game state

SnakeEngine handles input handling and game loop
1. passes input to Snake object to update game state
2. updated game state is sent to board to render

SnakeBoard handles rendering, abstracting away curse module
1. it renders the board
2. renders snake body
3. renders food

Instead of rendering row by row, can just update the necessary pixel changes
1. Delete tail pixel
2. Create new head pixel
3. Create new food pixel if eaten


