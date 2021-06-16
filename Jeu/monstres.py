import pygame
import core
from pygame.math import Vector2
import random
from time import sleep


class Monstres:
    def __init__(self):
        self.taille = 12
        self.directionB = Vector2(-1, 0)
        self.positionB = Vector2(236, 265)

        self.directionC = Vector2(-1, 0)
        self.positionC = Vector2(278, 220)

        self.directionI = Vector2(-1, 0)
        self.positionI = Vector2(278, 249)

        self.directionP = Vector2(-1, 0)
        self.positionP = Vector2(278, 275)

        self.vitesse = 4
        self.condition = 0

    def manger(self, pacmann):
    # Blinky
        if self.positionB.x >= pacmann.position.x - 15 and self.positionB.x <= pacmann.position.x + 15 and self.positionB.y >= pacmann.position.y - 15 and self.positionB.y <= pacmann.position.y + 15:
            pacmann.nbvie = pacmann.nbvie - 1
            pacmann.position = Vector2(294, 406)
            self.positionB = Vector2(236, 265)
            if pacmann.score>= 10:
                self.positionC = Vector2(236, 265)
            if pacmann.score == 30:
                self.positionI = Vector2(236, 265)
            if pacmann.score == 50:
                self.positionP = Vector2(236, 265)
            pacmann.vitesse = 0
            self.vitesse = 0
            pacmann.direction = Vector2(0, 0)
            self.condition = 1
    # Clyde
        if self.positionC.x >= pacmann.position.x - 15 and self.positionC.x <= pacmann.position.x + 15 and self.positionC.y >= pacmann.position.y - 15 and self.positionC.y <= pacmann.position.y + 15:
            pacmann.nbvie = pacmann.nbvie - 1
            pacmann.position = Vector2(294, 406)
            self.positionB = Vector2(236, 265)
            if pacmann.score >= 10:
                self.positionC = Vector2(236, 265)
            if pacmann.score == 30:
                self.positionI = Vector2(236, 265)
            if pacmann.score == 50:
                self.positionP = Vector2(236, 265)
            pacmann.vitesse = 0
            self.vitesse = 0
            pacmann.direction = Vector2(0, 0)
            self.condition = 1

    # Inky
        if self.positionI.x >= pacmann.position.x - 15 and self.positionI.x <= pacmann.position.x + 15 and self.positionI.y >= pacmann.position.y - 15 and self.positionI.y <= pacmann.position.y + 15:
            pacmann.nbvie = pacmann.nbvie - 1
            pacmann.position = Vector2(294, 406)
            self.positionB = Vector2(236, 265)
            if pacmann.score >= 10:
                self.positionC = Vector2(236, 265)
            if pacmann.score == 30:
                self.positionI = Vector2(236, 265)
            if pacmann.score == 50:
                self.positionP = Vector2(236, 265)
            pacmann.vitesse = 0
            self.vitesse = 0
            pacmann.direction = Vector2(0, 0)
            self.condition = 1
    # Pinky
        if self.positionP.x >= pacmann.position.x - 15 and self.positionP.x <= pacmann.position.x + 15 and self.positionP.y >= pacmann.position.y - 15 and self.positionP.y <= pacmann.position.y + 15:
            pacmann.nbvie = pacmann.nbvie - 1
            pacmann.position = Vector2(294, 406)
            self.positionB = Vector2(236, 265)
            if pacmann.score >= 10:
                self.positionC = Vector2(236, 265)
            if pacmann.score == 30:
                self.positionI = Vector2(236, 265)
            if pacmann.score == 50:
                self.positionP = Vector2(236, 265)
            pacmann.vitesse = 0
            self.vitesse = 0
            pacmann.direction = Vector2(0, 0)
            self.condition = 1

    def orientation(self, murss,pac):
        bas = [0, 1]
        haut = [0, -1]
        gauche = [-1, 0]
        droite = [1, 0]
        horizontal = [gauche, droite]
        vertical = [bas, haut]


#### Blinky
        randhoriB = random.choice(horizontal)
        randvertiB = random.choice(vertical)
        # bas

        if self.directionB == Vector2(0, 1):
            if murss.map[int((self.positionB.x + self.directionB.x * self.vitesse) / (murss.longueur_case))][
                int(((self.positionB.y + self.directionB.y * self.vitesse) + 13) / (murss.longueur_case))] == 1:

                self.directionB = Vector2(randhoriB)
            else:
                self.positionB.x = self.positionB.x + (self.directionB.x * self.vitesse)
                self.positionB.y = self.positionB.y + (self.directionB.y * self.vitesse)
        # haut
        elif self.directionB == Vector2(0, -1):
            if murss.map[int((self.positionB.x + self.directionB.x * self.vitesse) / (murss.longueur_case))][
                int(((self.positionB.y + self.directionB.y * self.vitesse) - 10) / (murss.longueur_case))] == 1:

                self.directionB = Vector2(randhoriB)
            else:
                self.positionB.x = self.positionB.x + (self.directionB.x * self.vitesse)
                self.positionB.y = self.positionB.y + (self.directionB.y * self.vitesse)

        # gauche
        elif self.directionB == Vector2(-1, 0):
            if murss.map[int(((self.positionB.x + self.directionB.x * self.vitesse) - 13) / (murss.longueur_case))][
                int((self.positionB.y + self.directionB.y * self.vitesse) / (murss.longueur_case))] == 1:
                self.directionB = Vector2(randvertiB)
            else:
                self.positionB.x = self.positionB.x + (self.directionB.x * self.vitesse)
                self.positionB.y = self.positionB.y + (self.directionB.y * self.vitesse)

        # droite
        elif self.directionB == Vector2(1, 0):
            if murss.map[int(((self.positionB.x + self.directionB.x * self.vitesse) + 13) / (murss.longueur_case))][
                int((self.positionB.y + self.directionB.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[
                int(((self.positionB.x + self.directionB.x * self.vitesse) + 13) / (murss.longueur_case))][
                int((self.positionB.y + self.directionB.y * self.vitesse) / (murss.longueur_case))] == 4:
                self.directionB = Vector2(randvertiB)
            else:
                self.positionB.x = self.positionB.x + (self.directionB.x * self.vitesse)
                self.positionB.y = self.positionB.y + (self.directionB.y * self.vitesse)

#### Clyde
        randhoriC = random.choice(horizontal)
        randvertiC = random.choice(vertical)
        # bas
        if pac.score>=10:
            if self.directionC == Vector2(0, 1):
                if murss.map[int((self.positionC.x + self.directionC.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionC.y + self.directionC.y * self.vitesse) + 13) / (murss.longueur_case))] == 1:

                    self.directionC = Vector2(randhoriC)
                else:
                    self.positionC.x = self.positionC.x + (self.directionC.x * self.vitesse)
                    self.positionC.y = self.positionC.y + (self.directionC.y * self.vitesse)
            # haut
            elif self.directionC == Vector2(0, -1):
                if murss.map[int((self.positionC.x + self.directionC.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionC.y + self.directionC.y * self.vitesse) - 10) / (murss.longueur_case))] == 1:

                    self.directionC = Vector2(randhoriC)
                else:
                    self.positionC.x = self.positionC.x + (self.directionC.x * self.vitesse)
                    self.positionC.y = self.positionC.y + (self.directionC.y * self.vitesse)

            # gauche
            elif self.directionC == Vector2(-1, 0):
                if murss.map[int(((self.positionC.x + self.directionC.x * self.vitesse) - 13) / (murss.longueur_case))][
                    int((self.positionC.y + self.directionC.y * self.vitesse) / (murss.longueur_case))] == 1:

                    self.directionC = Vector2(randvertiC)
                else:
                    self.positionC.x = self.positionC.x + (self.directionC.x * self.vitesse)
                    self.positionC.y = self.positionC.y + (self.directionC.y * self.vitesse)

            # droite
            elif self.directionC == Vector2(1, 0):
                if murss.map[int(((self.positionC.x + self.directionC.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionC.y + self.directionC.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[
                    int(((self.positionC.x + self.directionC.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionC.y + self.directionC.y * self.vitesse) / (murss.longueur_case))] == 4:
                    self.directionC = Vector2(randvertiC)
                else:
                    self.positionC.x = self.positionC.x + (self.directionC.x * self.vitesse)
                    self.positionC.y = self.positionC.y + (self.directionC.y * self.vitesse)


#### Inky
        randhoriI = random.choice(horizontal)
        randvertiI = random.choice(vertical)
        # bas
        if pac.score>=30:
            if self.directionI == Vector2(0, 1):
                if murss.map[int((self.positionI.x + self.directionI.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionI.y + self.directionI.y * self.vitesse) + 13) / (murss.longueur_case))] == 1:

                    self.directionI = Vector2(randhoriI)
                else:
                    self.positionI.x = self.positionI.x + (self.directionI.x * self.vitesse)
                    self.positionI.y = self.positionI.y + (self.directionI.y * self.vitesse)
            # haut
            elif self.directionI == Vector2(0, -1):
                if murss.map[int((self.positionI.x + self.directionI.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionI.y + self.directionI.y * self.vitesse) - 10) / (murss.longueur_case))] == 1:

                    self.directionI = Vector2(randhoriI)
                else:
                    self.positionI.x = self.positionI.x + (self.directionI.x * self.vitesse)
                    self.positionI.y = self.positionI.y + (self.directionI.y * self.vitesse)

            # gauche
            elif self.directionI == Vector2(-1, 0):
                if murss.map[int(((self.positionI.x + self.directionI.x * self.vitesse) - 13) / (murss.longueur_case))][
                    int((self.positionI.y + self.directionI.y * self.vitesse) / (murss.longueur_case))] == 1:

                    self.directionI = Vector2(randvertiI)
                else:
                    self.positionI.x = self.positionI.x + (self.directionI.x * self.vitesse)
                    self.positionI.y = self.positionI.y + (self.directionI.y * self.vitesse)

            # droite
            elif self.directionI == Vector2(1, 0):
                if murss.map[int(((self.positionI.x + self.directionI.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionI.y + self.directionI.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[
                    int(((self.positionI.x + self.directionI.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionI.y + self.directionI.y * self.vitesse) / (murss.longueur_case))] == 4:
                    self.directionI = Vector2(randvertiI)
                else:
                    self.positionI.x = self.positionI.x + (self.directionI.x * self.vitesse)
                    self.positionI.y = self.positionI.y + (self.directionI.y * self.vitesse)


#### Pinky
        randhoriP = random.choice(horizontal)
        randvertiP = random.choice(vertical)
        # bas
        if pac.score>=50:
            if self.directionP == Vector2(0, 1):
                if murss.map[int((self.positionP.x + self.directionP.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionP.y + self.directionP.y * self.vitesse) + 13) / (murss.longueur_case))] == 1:

                    self.directionP = Vector2(randhoriP)
                else:
                    self.positionP.x = self.positionP.x + (self.directionP.x * self.vitesse)
                    self.positionP.y = self.positionP.y + (self.directionP.y * self.vitesse)
            # haut
            elif self.directionP == Vector2(0, -1):
                if murss.map[int((self.positionP.x + self.directionP.x * self.vitesse) / (murss.longueur_case))][
                    int(((self.positionP.y + self.directionP.y * self.vitesse) - 10) / (murss.longueur_case))] == 1:

                    self.directionP = Vector2(randhoriP)
                else:
                    self.positionP.x = self.positionP.x + (self.directionP.x * self.vitesse)
                    self.positionP.y = self.positionP.y + (self.directionP.y * self.vitesse)

            # gauche
            elif self.directionP == Vector2(-1, 0):
                if murss.map[int(((self.positionP.x + self.directionP.x * self.vitesse) - 13) / (murss.longueur_case))][
                    int((self.positionP.y + self.directionP.y * self.vitesse) / (murss.longueur_case))] == 1:

                    self.directionP = Vector2(randvertiP)
                else:
                    self.positionP.x = self.positionP.x + (self.directionP.x * self.vitesse)
                    self.positionP.y = self.positionP.y + (self.directionP.y * self.vitesse)

            # droite
            elif self.directionP == Vector2(1, 0):
                if murss.map[int(((self.positionP.x + self.directionP.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionP.y + self.directionP.y * self.vitesse) / (murss.longueur_case))] == 1 or murss.map[
                    int(((self.positionP.x + self.directionP.x * self.vitesse) + 13) / (murss.longueur_case))][
                    int((self.positionP.y + self.directionP.y * self.vitesse) / (murss.longueur_case))] == 4:
                    self.directionP = Vector2(randvertiP)
                else:
                    self.positionP.x = self.positionP.x + (self.directionP.x * self.vitesse)
                    self.positionP.y = self.positionP.y + (self.directionP.y * self.vitesse)