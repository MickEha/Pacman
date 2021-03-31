# Mickael Ehanno, Maxence Dien
# ehannomickael@gmail.com
# C'est un programme pour le jeu Pac-Man
import core
from Jeu.grossepastille import GrossePastille
from Jeu.mur import Mur
from Jeu.pacman import Pacman


#V Globale
from Jeu.pastille import Pastille

joueur = Pacman()
pastille = Pastille()
grossepastille = GrossePastille()
wall = Mur()



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [600, 600]

    print("Setup END-----------")


def run():

    #affichage
    pastille.afficher(core)
    wall.afficher(core)
    joueur.afficher(core)


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



    #update
    joueur.bouger()


if __name__ == '__main__':
    # Mon programme
    print("test")
    core.main(setup, run)
