from pygame import font, time
from threading import Thread


class FPSCounter:
    def __init__(self, font_size=36, font_color=(50, 50, 50)):
        self.fps_holder = 0  # F
        self.fps_history = [0 for i in range(10)]
        self.fps_calm = 0

        self.FONT = font.SysFont("", font_size)
        self.font_color = font_color
        
        self.running = True
        Thread(target=self.count_fps).start()

    def update(self, new_time):
        self.fps_history.pop(0)
        self.fps_history.append(1000/(max(1, new_time - self.fps_holder)))
        self.fps_holder = new_time

    def count_fps(self):
        while self.running:
            self.fps_calm = round(sum(self.fps_history)/len(self.fps_history))
            time.wait(500)

    def get_fps_label(self):
        return self.FONT.render(str(self.fps_calm), True, self.font_color)
