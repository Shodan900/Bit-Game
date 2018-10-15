from setup import *
from Bullet import *
class Ship:
    image = pygame.image.load("ship.gif")
    rotation = 0
    WIDTH = image.get_rect().size[0]
    health = 100
    HEIGHT = image.get_rect().size[1]
    delayer = 0
    def __init__(self):
        self.pos = {
            "x": WIDTH / 2,
            "y": HEIGHT - self.HEIGHT
        }
    def update(self):
        if self.pos["x"] > (500 - self.WIDTH):
            self.pos["x"] = 500 - self.WIDTH
        if self.pos["y"] > (500 - self.HEIGHT):
            self.pos["y"] = 500 - self.HEIGHT
        if self.pos["x"] < 0:
            self.pos["x"] = 0
        if self.pos["y"] < 0:
            self.pos["y"] = 0
        self.image = pygame.transform.rotate(self.image, self.rotation)
        DISPLAY.blit(self.image, (self.pos["x"], self.pos["y"]))

ship = Ship()