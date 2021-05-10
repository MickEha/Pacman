import pygame
import core
from pygame.math import Vector2
import random
from time import sleep


class Monstres:
    def __init__(self):
        self.taille = 12
        self.position = Vector2(236, 265)
        self.direction = Vector2(-1, 0)
        self.vitesse = 4
        self.condition=0





    def manger(self,pacmann):
        if self.position.x >= pacmann.position.x-15 and self.position.x <= pacmann.position.x+15 and self.position.y >= pacmann.position.y-15 and self.position.y <= pacmann.position.y+15:
            pacmann.nbvie=pacmann.nbvie-1
            pacmann.position = Vector2(294,406)
            self.position = Vector2(236, 265)
            pacmann.vitesse=0
            self.vitesse=0
            pacmann.direction = Vector2(0,0)
            self.condition=1






    def orientation(self,murss):
        bas = [0, 1]
        haut = [0, -1]
        gauche = [-1, 0]
        droite = [1, 0]
        horizontal=[gauche, droite]
        vertical=[bas, haut]
        randhori = random.choice(horizontal)
        randverti = random.choice(vertical)
#bas
        if self.direction==Vector2(0,1):
            if murss.map[int((self.position.x + self.direction.x * self.vitesse) / (murss.longueur_case))][int(((self.position.y + self.direction.y * self.vitesse)+13) / (murss.longueur_case))] == 1 or murss.map[int((self.position.x + self.direction.x * self.vitesse) / (murss.longueur_case))][int(((self.position.y + self.direction.y * self.vitesse)+13) / (murss.longueur_case))] == 4:

                self.direction=Vector2(randhori)
            else:
                self.position.x = self.position.x + (self.direction.x * self.vitesse)
                self.position.y = self.position.y + (self.direction.y * self.vitesse)
#haut
        elif self.direction==Vector2(0,-1):
            if murss.map[int((self.position.x + self.direction.x * self.vitesse) / (murss.longueur_case))][int(((self.position.y + self.direction.y * self.vitesse)-10) / (murss.longueur_case))] == 1 or murss.map[int((self.position.x + self.direction.x * self.vitesse) / (murss.longueur_case))][int(((self.position.y + self.direction.y * self.vitesse)-10) / (murss.longueur_case))] == 4:

                self.direction=Vector2(randhori)
            else:
                self.position.x = self.position.x + (self.direction.x * self.vitesse)
                self.position.y = self.position.y + (self.direction.y * self.vitesse)

#gauche
        elif self.direction==Vector2(-1,0):
            if murss.map[int(((self.position.x + self.direction.x * self.vitesse)-13) / (murss.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[int(((self.position.x + self.direction.x * self.vitesse)-13) / (murss.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murss.longueur_case))] == 4:

                self.direction=Vector2(randverti)
            else:
                self.position.x = self.position.x + (self.direction.x * self.vitesse)
                self.position.y = self.position.y + (self.direction.y * self.vitesse)

#droite
        elif self.direction==Vector2(1,0):
            if murss.map[int(((self.position.x + self.direction.x * self.vitesse)+13) / (murss.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[int(((self.position.x + self.direction.x * self.vitesse)+13) / (murss.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murss.longueur_case))] == 4:
                self.direction=Vector2(randverti)
            else:
                self.position.x = self.position.x + (self.direction.x * self.vitesse)
                self.position.y = self.position.y + (self.direction.y * self.vitesse)

