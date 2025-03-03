



class Snake:

    def __init__(self, rows=128, cols=128):
        self.snake_head = None
        self.snake_body = None
        self.food = None
        self.ROWS = rows
        self.COLS = cols

    def move(direction) -> None:
        # update head to new location
        next_coord = self.get_next_coord(direction)
        if is_collision(next_coord):
            return
        if is_eat_food(next_coord):
            self.points += 1
            self.spawn_new_food()
        else:
            self.snake_body.popleft()

    def spawn_new_food() -> None:
        pass

    def is_collision(self, next_coord: Point) -> bool:
        if (next_coord.x < 0 or next_coord.x >= self.COLS or
            next_coord.y < 0 or next_coord.y >= self.ROWS):
            return True
        if next_coord in self.snake_body:
            return True
        return False 

    def is_eat_food() -> bool:
        pass


