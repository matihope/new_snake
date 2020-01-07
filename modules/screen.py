class Screen:
    def __init__(self):
        self.button_dict = {}
        self.custom_drawable = {}

        self.drawable_dicts = [self.button_dict, self.custom_drawable]
        self.sorted_draw_list = []

    def update(self, mouse):
        for button in self.button_dict.keys():
            button.update(mouse.get_pos()[0], mouse.get_pos()[1], mouse.get_pressed()[0])

    def draw(self, surface):
        for obj, _ in self.sorted_draw_list:
            obj.draw(surface)

    def add_button(self, button, draw_order=0):
        """Adds a single button to the screen"""
        self.button_dict[button] = draw_order
        self.update_sorted_draw_list()

    def add_buttons(self, button_dict):
        """
        Adds multiple buttons to the screen from dictionary, of button and draw_order.
        ex. menu.add_buttons({button1: '0', button2: '0', button3: '1'})
        """
        for button, draw_order in button_dict:
            self.button_dict[button] = draw_order
        self.update_sorted_draw_list()

    def add_custom_drawable(self, obj, draw_order=0):
        """Adds single button to the screen"""
        self.custom_drawable[obj] = draw_order
        self.update_sorted_draw_list()

    def update_sorted_draw_list(self):
        """ update the list with objects to draw, and sort with ascending order"""
        self.sorted_draw_list = []
        for dct in self.drawable_dicts:
            for pair in dct.items():
                self.sorted_draw_list.append(pair)

        self.sorted_draw_list.sort(key=lambda x: x[1])
