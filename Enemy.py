from setup import *

class Enemy:
    image = pygame.image.load("Enemy.gif")
    WIDTH = image.get_rect().size[0]
    HEIGHT = image.get_rect().size[1]
    health = 100
    timer = 0

    def destroy(self):
        enemies.remove(self)
        return True

    def __init__(self, x, y):
        self.pos = {
            "x": x,
            "y": y
        }

    def update(self):
        self.timer += 1
        if self.timer == 50:
            self.image = pygame.image.load("Enemy.gif")
            self.timer = 0
        self.pos["y"] += 0.1

        DISPLAY.blit(self.image, (self.pos["x"] + self.WIDTH / 2, self.pos["y"]))
        if self.pos["y"] > HEIGHT:
            self.destroy()
            return True