import pygame
import core
from pygame.math import Vector2

class Pastille:
    def __init__(self):
        self.taille = 4
        self.R = 210
        self.G = 105
        self.B = 30
        self.position = Vector2(50,50)

    def afficher(self,core):
        pygame.draw.circle(core.screen, (self.R, self.G, self.B), (self.position.x, self.position.y), self.taille)


