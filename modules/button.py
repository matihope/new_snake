import pygame

pygame.font.init()


class DictButton(type):
    _list = None

    def __iter__(cls):
        return iter(cls._list.items())

    def __getitem__(cls, key):
        return cls._list[key]


class Button(metaclass=DictButton):
    _list = {}

    def __init__(self, x, y, width=100, height=50, align_x='center', align_y='center',
                 colors=((220, 100, 100), (180, 100, 100), (120, 100, 100)),
                 text="", font_size=36, font_colors=((220, 220, 220), (180, 220, 220), (120, 180, 180)),
                 trigger=None, long_press=True, tag=str(len(_list))):
        self._list[tag] = self

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.align_x = align_x
        self.align_y = align_y
        self.colors = colors
        self.text = text
        self.font_colors = font_colors

        self.draw_x = self.x - self.width//2  # Default align_x='center'
        self.draw_y = self.y - self.height//2  # Default align_y='center'
        if align_x == 'left':
            self.draw_x = self.x
        elif align_x == 'right':
            self.draw_x = self.x + self.width
        if align_y == 'top':
            self.draw_y = self.y
        elif align_y == 'bottom':
            self.draw_y = self.y + self.height

        self.font = pygame.font.SysFont('', font_size)
        self.body = pygame.Surface((self.width, self.height))

        self.long_press = long_press
        self.__pressed_last_update = False
        self.pressed = False
        self.enabled = True
        self.visible = True

        self.trigger = trigger

    def update(self, mouse_x, mouse_y, mouse_press):
        if self.enabled:

            self.__pressed_last_update = self.pressed
            self.pressed = False

            col = 0
            if self.is_hovering(mouse_x, mouse_y):
                col = 2 if mouse_press else 1

                self.pressed = mouse_press

                if mouse_press and self.trigger is not None:
                    if self.long_press:
                        self.trigger()
                    else:
                        if not self.__pressed_last_update:
                            self.trigger()

            self.body.fill(self.colors[col])

            text_surf = self.font.render(self.text, True, self.font_colors[col])
            self.body.blit(text_surf, (self.body.get_width()//2-text_surf.get_width()//2,
                                       self.body.get_height()//2-text_surf.get_height()//2))

    def draw(self, surface):
        if self.visible:
            surface.blit(self.body, (self.draw_x, self.draw_y))

    def is_hovering(self, mouse_x, mouse_y):
        if mouse_x < self.draw_x:
            return False
        elif self.draw_x + self.width < mouse_x:
            return False
        elif mouse_y < self.draw_y:
            return False
        elif self.draw_y + self.height < mouse_y:
            return False
        return True
