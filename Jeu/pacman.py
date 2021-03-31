import pygame
import core
from pygame.math import Vector2

class Pacman:
    def __init__(self):
        self.taille = 12
        self.R = 255
        self.G = 215
        self.B = 0
        self.position = Vector2(294,406)
        self.direction = Vector2(0,0)
        self.vitesse = 5


    def afficher(self,core):
        pygame.draw.circle(core.screen, (self.R, self.G, self.B), (self.position.x, self.position.y), self.taille)






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

    def bouger(self,murs):
            if murs.map [int((self.position.x+self.direction.x*self.vitesse)/(murs.longueur_case))][int((self.position.y+self.direction.y*self.vitesse)/(murs.longueur_case))] == 1:
                self.direction=Vector2()

            else:
                self.position.x=self.position.x+ (self.direction.x*self.vitesse)
                self.position.y = self.position.y + (self.direction.y*self.vitesse)

    def manger(self,murs):
        if murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] == 2:
            pass
    def collision(self):
        pass
