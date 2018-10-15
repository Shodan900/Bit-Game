import pygame
import math
from pygame import *

from Ship import *
from setup import *
class Bullet:
    char = '>>'
    font = pygame.font.Font("Minecraftia.ttf", 16)
    fontRender = font.render(char, False, (96,217,241))
    fontRender = pygame.transform.rotate(fontRender, 90)

    def __init__(self, x, y):
        self.pos = {
            "x": x,
            "y": y
        }
        bulletsound.play(0, 0)

    def destroy(self):
        bullets.remove(self)

    def update(self):
        self.pos["y"] -= 1
        if self.pos["y"] < 0:
            self.destroy()
        for i in enemies:
            if i.pos["y"] + i.HEIGHT > self.pos["y"] and i.pos["y"] < self.pos["y"] and i.pos["x"] < self.pos["x"] and i.pos["x"] + i    .HEIGHT > self.pos["x"]:
                i.image = pygame.image.load("Enemyhit.gif")
                hitsound.play(0, 0 )
                i.health -= 20
                if i.health < 0:
                    i.destroy()
                    return True
                self.destroy()
        DISPLAY.blit(self.fontRender, (self.pos["x"], self.pos["y"]))