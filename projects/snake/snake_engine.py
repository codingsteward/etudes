# Snake Engine

import curses
from enum import Enum

class SnakePixel(Enum):
    HORIZONTAL = '═'
    VERTICAL = '║'
    NORTH_WEST = '╝'
    SOUTH_WEST = '╗'
    NORTH_EAST = '╚'
    SOUTH_EAST = '╔'

class SnakeBoard: # a curse window
    def __init__(self, width=17, height=13):
        self.width = 17
        self.height = 13
        self.setup()

    def setup(self):
        curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.window = curses.newwin(self.height, self.width)
        self.window.clear()
        self.window.border()
        self.window.nodelay(True)
        self.window.refresh()

    def cleanup(self):
        print("Cleaning up...")
        curses.nocbreak()
        curses.echo()
        curses.endwin()


    def update_pixel(self, x, y, val):
        self.window.addstr(y, x, val)

    def draw_snake(self, remove_pixels=[], add_pixels=[]):
        for x, y in remove_pixels:
            self.update_pixel(x, y, '')

        for x, y in add_pixels:
            pixel = SnakePixel.HORIZONTAL.value
            self.update_pixel(x, y, pixel)

    def draw_food(self, x, y):
        self.update_pixel(x, y, '@')

    def render(self):
        self.window.refresh()

class Snake:

    def __init__(self):
        self.snake = []
        self.food = []
        self.head_pos = []
        self.points = 0

    def move(self, direction): # move snake, return updated pixels

        removed_states, added_states = [], []

        # new_pos = (x, y)

        return removed_states, added_states

class SnakeEngine:
    """Handles the game engine loop, fetch input, update state and render new state"""

    def __init__(self):
        self.board = SnakeBoard()
        self.snake = Snake()
        self.board.draw_snake(add_pixels=[(2, 1), (2, 2), (2, 3)])
        self.board.draw_food(5, 5)
        self.board.render()


    def start(self):
        # wait for input
        try:
            while True:
                pass
            self.board.cleanup()
        finally:
            self.cleanup()

    def cleanup(self):
        self.board.cleanup()

if __name__ == "__main__":
    snake_game = SnakeEngine()
    try:
        snake_game.start()
    except KeyboardInterrupt:
        print("keyboard interrupt")
        snake_game.cleanup()
