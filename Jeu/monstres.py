import pygame
import core
from pygame.math import Vector2

class Monstres:
    def __init__(self):
        self.taille = 12
        self.R = 255
        self.G = 215
        self.B = 0
        self.position = Vector2(200, 200)
        self.direction = Vector2(0, 0)
        self.vitesse = 5


    def afficher(self,core):
      pass


    def manger(self):
        pass

    def mourir(self):
        pass

    def orientation(self):
        pass

    def collision(self):
        pass