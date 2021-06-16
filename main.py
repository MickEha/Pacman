# Mickael Ehanno, Maxence Dien
# ehannomickael@gmail.com
# C'est un programme pour le jeu Pac-Man

import core
from Jeu import pacman
from Jeu.fenetredejeu import Fenetredejeu
from Jeu.monstres import Monstres
from Jeu.mur import Mur
from Jeu.pacman import Pacman


#V Globale
joueur = Pacman()
wall = Mur()
mob=Monstres()
game=Fenetredejeu()



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [615, 600]
    print("Setup END-----------")


def run():

    #affichage
    game.afficher(core,joueur,mob,wall)







    #clavier
    if core.getkeyPress():
        if core.getkeyPressValue()==1073741905:
            joueur.orientation("DOWN")
        elif core.getkeyPressValue()==1073741904:
            joueur.orientation("LEFT")
        elif core.getkeyPressValue()==1073741906:
            joueur.orientation("UP")
        elif core.getkeyPressValue()==1073741903:
            joueur.orientation("RIGHT")
        elif core.getkeyPressValue()==32:
                game.reset=1




    #update
    joueur.bouger(wall)
    joueur.manger(wall)
    game.score(joueur)
    mob.orientation(wall,joueur)
    game.fin(joueur,mob)
    mob.manger(joueur)
    game.mourir(joueur,mob)
    joueur.reset(mob)
    game.debut(joueur,mob,wall,value=0)








if __name__ == '__main__':
    # Mon programme
    core.main(setup, run)
