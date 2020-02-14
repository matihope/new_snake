from pygame import K_a, K_d, K_w, K_s
from time import sleep
from threading import Thread


class Snake:
    def __init__(self, x, y, tile_size, head_surface, body_surface, mps):
        self.x, self.y = x * tile_size, y * tile_size
        self.tile_size = tile_size
        self.dead = False
        self.head_surface, self.body_surface = head_surface, body_surface
        self.body = [(self.x, self.y)]

        self.points = 0
        self.move_h, self.move_v = 0, 0
        self.mps = mps
        Thread(target=self.move).start()

    def pos(self):
        return self.x, self.y

    def score(self):
        self.body.append((self.body[-1][0], self.body[-1][1]))
        self.points += 1

    def change_dir(self, keys):
        if keys[K_s] or keys[K_w]:
            self.move_v = (int(keys[K_s]) - int(keys[K_w]))
            self.move_h = 0

        elif keys[K_d] or keys[K_a]:
            self.move_h = (int(keys[K_d]) - int(keys[K_a]))
            self.move_v = 0

    def move(self):
        # Independently processed function, runs mps times per second
        # for call look in __init__
        while not self.dead:
            self.body.pop(0)
            self.body.append((self.x, self.y))

            self.x += self.move_h * self.tile_size
            self.y += self.move_v * self.tile_size

            sleep(1/self.mps)

    def draw(self, surface):
        # Body
        for part_x, part_y in self.body[1:]:
            surface.blit(self.body_surface, (part_x, part_y))
        # Head
        surface.blit(self.head_surface, (self.x, self.y))
