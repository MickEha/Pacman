import pygame
import core
from pygame.math import Vector2

class Pacman:
    def __init__(self):
        self.taille = 25
        self.R = 255
        self.G = 215
        self.B = 0
        self.position = Vector2(200,200)
        self.direction = Vector2(0,0)
        self.vitesse = 5


    def afficher(self,core):
        pygame.draw.circle(core.screen, (self.R, self.G, self.B), (self.position.x, self.position.y), self.taille)

    def manger(self):
        pass

    def mourir(self):
        pass

    def orientation(self,value):
        if value=="DOWN":
            self.direction=Vector2(0,1)
        elif value=="UP":
            self.direction=Vector2(0,-1)
        elif value == "LEFT":
            self.direction = Vector2(-1, 0)
        elif value == "RIGHT":
            self.direction = Vector2(1, 0)

    def bouger(self):
        self.position.x=self.position.x+ (self.direction.x*self.vitesse)
        self.position.y = self.position.y + (self.direction.y*self.vitesse)


    def collision(self):
        pass
