import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sounds/tron.mp3")
pygame.mixer.music.play(-1,0.0)
WIDTH = 500
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
bullets = []
enemies = []
particles = []

bulletsound = pygame.mixer.Sound("sounds/shoot.wav")
hitsound = pygame.mixer.Sound("sounds/hit.wav")