import random

Table_gain = {"ICJC":[3,3],"ICJD":[0,5],"IDJC": [5,0],"IDJD":[2,2]}

Stratégie = ["All-D", "Random", "Tit-for-tat", "Tester", "Joss"]

def affiche_coup(strat1, strat2):
    print(" "*3+start1.coup+" "*10+strat2.coup)

def Combat(strat1, strat2):
    print(strat1+ " "*10+ strat2)
    for i in range(200):
        strat1.choix(strat2.prec_coup)
        strat2.choix(strat1.prec_coup)

        affiche_coup(strat1, strat2)

        strat1.prec_coup = strat1.coup
        strat2.prec_coup = strat2.coup
                    
                
def main():
    strat1 = "All-D"
    strat2 = "Random"
    Combat(strat1, strat2)


main()
