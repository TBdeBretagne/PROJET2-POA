import random as r

r.seed(90)

class Agent:
    def __init__(self, indice, regle):
        self.nom = indice
        self.gainR = 0
        self.gainB = 0
        self.couleur_initial()
        self.Rouge = 0
        self.Bleu = 0
        self.choix_regle(regle)
        self.gagne = False
        self.Imitation = 0

    def couleur_initial(self):
        self.couleur = r.choice(["R", "B"])
        nbr = r.randint(0,100)
        if nbr < 10:
            self.Tetu = True
        else:
            self.Tetu = False

    def choix_regle(self, regle):
        self.regle = r.choice(regle)
        
    def Memoire(self, A):
        nbr = r.randint(0,100)
        if nbr < 5:
            self.Rouge = 0
            self.Bleu = 0
        
        if(A.couleur == "R"):
            self.Rouge += 1
        else:
            self.Bleu += 1
    
class Population:
    def __init__(self, nbr, regle):
        if(nbr%2 != 0):
        #si le nombre d'agent est impaire, on ajoute 1 pour avoir un nombre pair
            nbr += 1
        self.nbr_agent = nbr
        self.L = []
        self.Rouge = 0
        self.Bleu = 0
        self.gainR = 0
        self.gainB = 0
        for i in range(nbr):
            self.L.append(Agent(i, regle))
            
    def afficher(self):
        for agent in self.L:
            print(agent.nom," ", end ="")
        print("")
        
    def melanger(self):
        r.shuffle(self.L)

    def memoire_commune(self):
        self.Rouge = 0 # Reset des valeurs
        self.Bleu = 0
        for A in self.L:
            if(A.regle == "Type"):
                self.Rouge += A.Rouge
                self.Bleu += A.Bleu

    def afficher_couleur(self):
        for A in self.L:
            print(A.nom, " :", A.couleur)

    def total_gain(self):
        for A in self.L:
            self.gainR += A.gainR
            self.gainB += A.gainB

        
    
