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

    def __init__(self, x, y, width=100, height=50, colors=((220, 100, 100), (180, 100, 100), (120, 100, 100)),
                 text="", font=36, font_colors=((220, 220, 220), (180, 220, 220), (120, 180, 180)),
                 trigger=None, tag=str(len(_list))):
        # assert(type(self.__list[tag]) is not Button)
        self._list[tag] = self

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors
        self.text = text
        self.font_colors = font_colors

        self.pressed = False
        self.enabled = True
        self.visible = True

        # font argument can either be pygame.font.Font or font size
        if font is pygame.font.Font:
            self.font = font
        else:
            self.font = pygame.font.SysFont("", font)

        self.trigger = trigger

        self.body = pygame.Surface((self.width, self.height))
        self.update(0, 0, False)

    def update(self, mouse_x, mouse_y, mouse_press):
        if self.enabled:

            self.pressed = False
            col = 0
            if self.is_hovering(mouse_x, mouse_y):
                self.pressed = mouse_press
                col = 2 if mouse_press else 1

                if mouse_press and self.trigger is not None:
                    self.trigger()

            self.body.fill(self.colors[col])

            text_surf = self.font.render(self.text, True, self.font_colors[col])
            self.body.blit(text_surf, (self.body.get_width()//2-text_surf.get_width()//2,
                                       self.body.get_height()//2-text_surf.get_height()//2))

    def draw(self, surface):
        if self.visible:
            surface.blit(self.body, (self.x, self.y))

    def is_hovering(self, mouse_x, mouse_y):
        if mouse_x < self.x:
            return False
        elif self.x + self.width < mouse_x:
            return False
        elif mouse_y < self.y:
            return False
        elif self.y + self.height < mouse_y:
            return False
        return True
