import pygame


class fenetredejeu:
    def __init__(self):
        self.Score=0
        self.ScoreMax=0
        self.nbVie=3
        self.Gameover=0
        self.Play=0

    def afficher(self,core):

        font = pygame.font.Font(None, 35)
        text = font.render("Score = ", 1, (0, 125, 125))
        core.screen.blit(text, (450,550))

        font = pygame.font.Font(None, 35)
        text = font.render("PacMan", 1, (255, 30, 30))
        core.screen.blit(text, (20, 550))


