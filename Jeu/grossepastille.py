import pygame
import core
from pygame.math import Vector2

class GrossePastille:
    def __init__(self):
        self.taille = 8
        self.R = 139
        self.G = 69
        self.B = 19
        self.position = Vector2(100,50)

    def afficher(self,core):
        pygame.draw.circle(core.screen, (self.R, self.G, self.B), (self.position.x, self.position.y), self.taille)


