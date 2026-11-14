import random

class Strategie:
    def __init__(self, name):
        self.nom = name # parmis "All-D", "Random", "Tit-for-tat", "Tester", "Joss", #Graduale, #Spiteful
        self.coup = "" # prochain coup
        self.prec_coup = "" # coup précédent
        self.indice = 0

        #Tester
        self.test = True
        self.tit_tat = False
    
        self.point = 0
        self.match_gagne = 0
        self.match_perdu = 0
        self.match_egalite = 0
        self.combat_gagne = 0
        self.combat_perdu = 0
        self.combat_egalite = 0

        #Graduale
        self.phase = "coop"
        self.nb_trahison = 0
        self.compteur = 0
        self.i = 0
        self.j = 0
        

        
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
            case "Graduale":
                if prec_adversaire == "":
                    self.coup = "C"  # Premier coup
                    return
                
                # Comptabilisation de chaque trahison adverse
                if prec_adversaire == "D":
                    self.nb_trahison += 1

                    if self.phase == "punition":
                        # La nouvelle trahison prolonge la punition
                        self.compteur += 1

                    elif self.phase != "reconciliation":
                        # Début d'une nouvelle séquence de punition
                        self.phase = "punition"
                        self.compteur = self.nb_trahison
                        self.i = 0
                        self.j = 0
                        
                if self.phase == "punition":
                    if self.i < self.compteur:
                        self.coup = "D"
                        self.i += 1

                    else:
                        self.phase = "reconciliation"

                # Phase de réconciliation
                if self.phase == "reconciliation":

                    if self.j < 2:
                        self.coup = "C"
                        self.j += 1

                    else:
                        self.phase = "cooperation"
                        self.coup = "C"

                # Phase de coopération normale
                elif self.phase == "cooperation":
                    self.coup = "C"
                    
            case "Spiteful":
                if prec_adversaire == "D":
                    self.nb_trahison += 1
                    
                if self.nb_trahison == 0:
                    self.coup = "C"

                else:
                    self.coup = "D"

                           
            case _:
                print("Strategie introuvable")

    def reinitialisation(self):
        self.point = 0
        self.indice = 0
        self.prec_coup = ""
        self.test = True
        self.tit_tat = False
        self.coup = ""

    def alea(self):
        alea = random.randint(0,99)
        if alea < 5:
            if self.coup == "D":
                self.coup = "C"
            else:
                self.coup = "D"
                    
