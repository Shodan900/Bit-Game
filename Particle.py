from setup import *


class Particle:
    def __init__(self):
        self.pos = {
            "x": random.randint(0, WIDTH),
            "y": 0
        }
        self.speed = random.randint(1, 2)

    def destroy(self):
        particles.remove(self)

    def update(self):
        self.pos["y"] += self.speed
        pygame.draw.line(DISPLAY, pygame.color.Color("purple"), (self.pos["x"], self.pos["y"]), (self.pos["x"], self.pos["y"] + random.randint(3, 10)), 3)
        if self.pos["y"] > HEIGHT:
            return True
