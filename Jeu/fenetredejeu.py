import pygame
import core


class Fenetredejeu:
    def __init__(self):
        pass

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
        core.screen.blit(mob_Blinky, (mob.position.x - 15, mob.position.y - 15))

        mob_Clyde = pygame.transform.scale(pygame.image.load("Ressources/Clyde.png"), (29, 29))
        core.screen.blit(mob_Clyde, (278, 220))
        if pac.score >= 5:
            core.screen.blit(mob_Clyde, (236 - 15, 265 - 15))

        mob_Inky = pygame.transform.scale(pygame.image.load("Ressources/Inky.png"), (29, 29))
        core.screen.blit(mob_Inky, (278, 249))

        mob_Pinky = pygame.transform.scale(pygame.image.load("Ressources/Pinky.png"), (29, 29))
        core.screen.blit(mob_Pinky, (278, 275))






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




    def fin(self,pac,mob):
        if pac.score==205 or pac.nbvie==0:
            mob.vitesse=0
            pac.vitesse = 0




    def mourir(self,pacman,mob):
            font = pygame.font.Font(None, 35)
            text = font.render("Vie = ", 1, (200, 100, 30))
            core.screen.blit(text, (300, 550))

            font = pygame.font.Font(None, 35)
            text = font.render(str(pacman.nbvie), 1, (200, 100, 30))
            core.screen.blit(text, (370, 550))

            if pacman.nbvie == 0:
                font = pygame.font.Font(None, 70)
                text = font.render("GAME OVER !!!!", 1, (255, 100, 255))
                core.screen.blit(text, (170, 250))





