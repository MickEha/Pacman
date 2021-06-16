import pygame
import core


class Fenetredejeu:
    def __init__(self):
        self.reset=0


    def afficher(self, core,pac,mob,mur):
        font = pygame.font.Font(None, 35)
        text = font.render("PacMan", 1, (255, 30, 30))
        core.screen.blit(text, (20, 550))

        font = pygame.font.Font(None, 35)
        text = font.render("Vie = ", 1, (200, 100, 30))
        core.screen.blit(text, (300, 550))

        ###MUR
        for i in range(22):
            for j in range(19):
                # Si c'est un mur, on trace un mur
                if (mur.map[i][j] == 1):
                    pygame.draw.rect(core.screen, (0, 0, 139), (i * mur.longueur_case, j * mur.longueur_case, 25, 25))
                # Sinon on laisse une case blanche
                elif (mur.map[i][j] == 0):
                    pygame.draw.rect(core.screen, (0, 0, 0), (i * mur.longueur_case, j * mur.longueur_case, 29, 30))

                elif (mur.map[i][j] == 2):
                    pygame.draw.circle(core.screen, (210, 105, 30),
                                       (i * mur.longueur_case + 13, j * mur.longueur_case + 13), 3)

                elif (mur.map[i][j] == 3):
                    pygame.draw.circle(core.screen, (139, 69, 19),
                                       (i * mur.longueur_case + 13, j * mur.longueur_case + 13), 7)

                elif (mur.map[i][j] == 4):
                    pygame.draw.rect(core.screen, (0, 150, 139), (i * mur.longueur_case, j * mur.longueur_case, 10, 25))



##PACMAN
        pygame.draw.circle(core.screen, (pac.R, pac.G, pac.B), (pac.position.x, pac.position.y), pac.taille)

##MONTRES
        mob_Blinky = pygame.transform.scale(pygame.image.load("Ressources/Blinky.png"), (29, 29))
        core.screen.blit(mob_Blinky, (mob.positionB.x - 15, mob.positionB.y - 15))

        mob_Clyde = pygame.transform.scale(pygame.image.load("Ressources/Clyde.png"), (29, 29))
        if pac.score == 10:
            mob.positionC.x=236
            mob.positionC.y=265
        if pac.score < 10:
            core.screen.blit(mob_Clyde, (278, 220))
        else:
            core.screen.blit(mob_Clyde, (mob.positionC.x - 15, mob.positionC.y - 15))

        mob_Inky = pygame.transform.scale(pygame.image.load("Ressources/Inky.png"), (29, 29))
        if pac.score == 30:
            mob.positionI.x=236
            mob.positionI.y=265
        if pac.score < 30:
            core.screen.blit(mob_Inky, (278, 249))
        else:
            core.screen.blit(mob_Inky, (mob.positionI.x - 15, mob.positionI.y - 15))


        mob_Pinky = pygame.transform.scale(pygame.image.load("Ressources/Pinky.png"), (29, 29))
        if pac.score == 50:
            mob.positionP.x=236
            mob.positionP.y=265
        if pac.score < 50:
            core.screen.blit(mob_Pinky, (278, 275))
        else:
            core.screen.blit(mob_Pinky, (mob.positionP.x - 15, mob.positionP.y - 15))


    def score(self,pacman):
        font = pygame.font.Font(None, 35)
        text = font.render("Score = ", 1, (0, 125, 125))
        core.screen.blit(text, (450, 550))

        font = pygame.font.Font(None, 35)
        text = font.render(str(pacman.score), 1, (0, 125, 125))
        core.screen.blit(text, (550, 550))

        if pacman.score == 205 :
            font = pygame.font.Font(None, 70)
            text = font.render("WIN !!!!", 1, (255, 100, 255))
            core.screen.blit(text, (200, 250))
            reset = pygame.font.Font(None, 40)
            restart = reset.render("Appuyez sur ESPACE pour relancer le jeu !!!!", 1, (0, 200, 0))
            core.screen.blit(restart, (30, 300))




    def fin(self,pac,mob):
        if pac.score==205 or pac.nbvie==-1:
            pac.vitesse = 0
            mob.vitesse=0


    def mourir(self,pacman,mob):
            font = pygame.font.Font(None, 35)
            text = font.render("Vie = ", 1, (200, 100, 30))
            core.screen.blit(text, (300, 550))

            font = pygame.font.Font(None, 35)
            text = font.render(str(pacman.nbvie), 1, (200, 100, 30))
            core.screen.blit(text, (370, 550))

            if pacman.nbvie == -1:
                font = pygame.font.Font(None, 70)
                text = font.render("GAME OVER !!!!", 1, (255, 100, 255))
                core.screen.blit(text, (140, 200))
                reset = pygame.font.Font(None, 40)
                restart = reset.render("Appuyez sur ESPACE pour relancer le jeu !!!!", 1, (0, 200, 0))
                core.screen.blit(restart, (30,300))


    def debut(self,pac,mob,murreset,value):
        if pac.score==205 or pac.nbvie==-1:
            if self.reset==1:
                pac.nbvie=2
                pac.score=0
                pac.vitesse = 4
                mob.vitesse = 4

                mob.positionB.x = 236
                mob.positionB.y = 265
                mob.directionB.x = -1
                mob.directionB.y = 0

                mob.positionC.x = 278
                mob.positionC.y = 220
                mob.directionC.x = -1
                mob.directionC.y = 0

                mob.positionI.x = 278
                mob.positionI.y = 249
                mob.directionI.x = -1
                mob.directionI.y = 0

                mob.positionP.x = 278
                mob.positionP.y = 275
                mob.directionP.x = -1
                mob.directionP.y = 0

                pac.position.x = 294
                pac.position.y = 406
                pac.direction.x = 0
                pac.direction.y = 0

                self.reset = 0
                murreset.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 1],
                            [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
                            [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
                            [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1],
                            [1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1],
                            [1, 1, 1, 1, 2, 1, 2, 1, 1, 4, 1, 1, 2, 1, 2, 1, 1, 1, 1],
                            [0, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 2, 2, 2, 0],
                            [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
                            [1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1],
                            [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
                            [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
                            [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
                            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1],
                            [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        else :
            self.reset = 0





