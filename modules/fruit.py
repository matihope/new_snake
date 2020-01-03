from random import randrange


class Fruit:
    def __init__(self, board_width, board_height, tile_size, body_surface):
        self.board_width, self.board_height = board_width, board_height
        self.tile_size = tile_size
        self.body_surface = body_surface

        self.x, self.y = 0, 0
        self.eat_fruit()

    def pos(self):
        return self.x, self.y

    def eat_fruit(self):
        self.x = randrange(0, self.board_width) * self.tile_size
        self.y = randrange(0, self.board_height) * self.tile_size

    def draw(self, surface):
        surface.blit(self.body_surface, (self.x, self.y))
