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
        self.vitesse = 4
        self.score= 0
        self.nbvie=3



    def reset(self,mob):
        if mob.position == Vector2(236, 265) and mob.condition==1:
            mob.vitesse=4
            self.vitesse=4
            mob.condition = 0

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
####   BAS
        if self.direction == Vector2(0, 1):
            if murs.map [int((self.position.x+self.direction.x*self.vitesse)/ murs.longueur_case)][int(((self.position.y + self.direction.y * self.vitesse)+14) / murs.longueur_case)] == 1:
                    self.direction=Vector2()

            else:
                    self.position.x = self.position.x + (self.direction.x * self.vitesse)
                    self.position.y = self.position.y + (self.direction.y * self.vitesse)


####   HAUT
        elif self.direction == Vector2(0,-1):
            if murs.map [int((self.position.x+self.direction.x*self.vitesse)/ murs.longueur_case)][
                int(((self.position.y + self.direction.y * self.vitesse)-11) / murs.longueur_case)] == 1:
                    self.direction=Vector2()

            else:
                    self.position.x = self.position.x + (self.direction.x * self.vitesse)
                    self.position.y = self.position.y + (self.direction.y * self.vitesse)


####   GAUCHE
        elif self.direction == Vector2(-1, 0):
            if murs.map [int(((self.position.x+self.direction.x*self.vitesse)-13)/ murs.longueur_case)][int((self.position.y + self.direction.y * self.vitesse) / murs.longueur_case)] == 1:
                    self.direction=Vector2()
            else:
                        self.position.x = self.position.x + (self.direction.x * self.vitesse)
                        self.position.y = self.position.y + (self.direction.y * self.vitesse)


####   DROITE
        elif self.direction == Vector2(1, 0):
            if murs.map [int(((self.position.x+self.direction.x*self.vitesse)+13)/ murs.longueur_case)][int((self.position.y + self.direction.y * self.vitesse) / murs.longueur_case)] == 1 or murs.map [int(((self.position.x+self.direction.x*self.vitesse)+13) / murs.longueur_case)][int((self.position.y + self.direction.y * self.vitesse) / murs.longueur_case)] == 4:
                    self.direction=Vector2()
            else:
                self.position.x = self.position.x + (self.direction.x * self.vitesse)
                self.position.y = self.position.y + (self.direction.y * self.vitesse)


    def manger(self,murs):
        #score pastille + 1
        if murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] == 2:
            self.score = self.score + 1

        # remettre à 0 la liste de pastille
        if murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] == 2:
            murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] = 0

        # score grosse pastille + 5
        if murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] == 3:
            self.score = self.score + 5

        # remettre à 0 la liste de grosse pastille
        if murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] == 3:
            murs.map[int((self.position.x + self.direction.x * self.vitesse) / (murs.longueur_case))][int((self.position.y + self.direction.y * self.vitesse) / (murs.longueur_case))] = 0



