import pygame
import core


class Fenetredejeu:
    def __init__(self):
        self.nbVie = 3
        self.Gameover = 0
        self.Play = 0

    def afficher(self, core):
        font = pygame.font.Font(None, 35)
        text = font.render("PacMan", 1, (255, 30, 30))
        core.screen.blit(text, (20, 550))

        font = pygame.font.Font(None, 35)
        text = font.render("Vie = ", 1, (200, 100, 30))
        core.screen.blit(text, (300, 550))

    def score(self,Pacman):
        font = pygame.font.Font(None, 35)
        text = font.render("Score = ", 1, (0, 125, 125))
        core.screen.blit(text, (450, 550))

        font = pygame.font.Font(None, 35)
        text = font.render(str(Pacman.score), 1, (255, 30, 30))
        core.screen.blit(text, (550, 550))

        if Pacman.score == 205 :
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





