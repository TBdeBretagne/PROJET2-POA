from agent import *

class Jeu:
    def __init__(self, nbr, gR, gB):
        self.gainR = gR
        self.gainB = gB
        self.Regle = ["recompense", "Type", "Majorite", "adaptation", "Imitation"]
        self.population = Population(nbr, self.Regle)
        self.nbrR = 0
        self.nbrB = 0
        
    def comparaison(self, A1, A2):
        if A1.couleur == A2.couleur :
            if A1.couleur == "R":
                A1.gainR += self.gainR
                A2.gainR += self.gainR
                A1.gagne = True
                A2.gagne = True
            else:
                A1.gainB += self.gainB
                A2.gainB += self.gainB
                A1.gagne = True
                A2.gagne = True
        else:
            A1.gagne = False
            A2.gagne = False
        A1.Memoire(A2)
        A2.Memoire(A1)
        A1.Immitation = A2.couleur
        A2.Immitation = A1.couleur

    def repartition(self):
        self.nbrR = 0 #Reset des valeurs
        self.nbrB = 0
        for p in self.population.L:
            c = p.couleur
            if c == "R":
                self.nbrR += 1
            else:
                self.nbrB += 1
        print("R =",self.nbrR,", B =",self.nbrB)

    def Tour(self):
        for i in range(0,self.population.nbr_agent, 2):
            self.comparaison(self.population.L[i], self.population.L[i+1])
        self.population.memoire_commune()
        self.population.total_gain()
        self.population.melanger()
        for A in self.population.L:
            self.RegleASuivre(A)
        self.repartition()

    def RegleASuivre(self, A):
        if A.Tetu == False:
            match A.regle:
                case "recompense":
                    if self.population.gainR > self.population.gainB:
                        A.couleur = "R"
                    elif self.population.gainR < self.population.gainB:
                        A.couleur = "B"
                    #else l'agent ne change pas de couleur

                case "Type":
                    if(self.population.Rouge > self.population.Bleu):
                        A.couleur = "R"
                    elif(self.population.Rouge < self.population.Bleu) :
                        A.couleur = "B"
                    #else : l'agent ne change pas de couleur
                case "Majorite":
                    if A.Rouge > A.Bleu:
                        A.couleur = "R"
                    elif A.Rouge < A.Bleu:
                        A.couleur = "B"
                    #else l'agent ne change pas de couleur
                case "adaptation":
                    if A.gagne == False:
                        if A.couleur == "R":
                            A.couleur = "B"
                        else:
                            A.couleur = "R"
                    #else l'agent ne change pas de couleur
                case "Imitation":
                    A.couleur = A.Imitation
