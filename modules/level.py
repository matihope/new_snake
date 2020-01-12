from modules import fruit, player
from modules.cf import collision


class SnakeGame:
    def __init__(self, size_x, size_y, tile_size, mps, bg, snake_head, snake_body, fruit_body):
        self.size_x, self.size_y = size_x, size_y
        self.tile_size = tile_size

        self.bg_color = bg

        self.snake = player.Snake(size_x/2, size_y/2, tile_size, snake_head, snake_body, mps)
        self.fruit = fruit.Fruit(size_x, size_y, tile_size, fruit_body)

    def handle_logic(self, keys):
        self.snake.change_dir(keys)
        if collision(self.snake.pos(), self.fruit.pos(), self.tile_size):
            self.snake.score()

            self.fruit.eat_fruit()
            while any([collision(part, self.fruit.pos(), self.tile_size) for part in self.snake.body]):
                self.fruit.eat_fruit()

        if not (0 <= self.snake.x < self.size_x * self.tile_size) or \
           not (0 <= self.snake.y < self.size_y * self.tile_size):
            self.snake.dead = True

        if any([collision(part, self.snake.pos(), self.tile_size) for part in self.snake.body[1:]]):
            self.snake.dead = True

    def draw(self, window):
        window.fill(self.bg_color)
        self.snake.draw(window)
        self.fruit.draw(window)
