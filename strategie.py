import random

class Strategie:
    def __init__(self, name):
        self.nom = name # parmis "All-D", "Random", "Tit-for-tat", "Tester", "Joss"
        self.coup = "" # prochain coup
        self.prec_coup = "" #coup precedent
        self.indice = 0
        self.test = True
        self.tit_tat = False
        self.point = 0
        self.match_gagne = 0
        self.match_perdu = 0
        self.match_egalite = 0
        self.combat_gagne = 0
        self.combat_perdu = 0
        self.combat_egalite = 0

        
    def choix(self, prec_adversaire):
        random.seed(42)  # Fixe la graine aléatoire
        match self.nom:
            case "All-D" :
                self.coup = "D"
            case "Random":
                self.coup = random.choice(["C","D"])
            case "Tit-for-tat":
                if prec_adversaire == "":
                    self.coup = "C"
                else:
                    self.coup = prec_adversaire
            case "Tester":
                if prec_adversaire == "":
                    self.coup = "D"
                elif (self.test and prec_adversaire == "D") or self.tit_tat:
                    self.tit_tat = True
                    self.coup = prec_adversaire
                else:
                    self.test = False
                    if self.indice == 2:
                        self.coup = "D"
                    else:
                        self.coup = "C"
                    self.indice = (self.indice + 1) % 3
                     
            case "Joss":
                if prec_adversaire == "":
                    self.coup = "C"
                else:
                    if self.indice == 0:
                        self.coup = "D"
                    else:
                        self.coup = prec_adversaire

                self.indice = (self.indice + 1) % 10
            case _:
                print("Strategie introuvable")

    def reinitialisation(self):
        self.point = 0
        self.prec_coup = ""
        self.indice = 0
        self.test = True
        self.tit_tat = False
        self.coup = ""
                    
