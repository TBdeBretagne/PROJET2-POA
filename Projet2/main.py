from jeu import *
import sys

def main(texte):
    J = Jeu(int(texte[1]), int(texte[2]), int(texte[3]))
    J.repartition()
    i = 1
    while(i == 1 or  (J.nbrR != 0 and J.nbrB != 0)):
        print("Tour ",i)
        J.Tour()
        if(len(texte) > 4):
            if(texte[4] == "-v"):
                J.population.afficher()
            if(texte[4] == "-vv"):
                J.population.afficher_couleur()
        i += 1
main(sys.argv)
