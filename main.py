import strategie as s
import sys

Table_gain = {"ICJC":[3,3],"ICJD":[0,5],"IDJC": [5,0],"IDJD":[2,2]}

Strat = ["All-D", "Random", "Tit-for-tat", "Tester", "Joss"]

def affiche_coup(strat1, strat2):
    print(" "*3+strat1.coup+" "*10+strat2.coup)

def resultat(participant):
    print("Resultat final : ")
    for strat in participant:
        print(strat.nom  + " : "+ "match gagne : "+ str(strat.match_gagne) + " match perdu : "+str(strat.match_perdu) + " match egalite : "+ str(strat.match_egalite) + " combat gagne : " + str(strat.combat_gagne) + " combat perdu : "+ str(strat.combat_perdu) + " combat egalite : "+ str(strat.combat_egalite))

def classement(participant):
    #tri a bulle
    for i in range(len(participant)):
        for j in range(len(participant)-1):
            if participant[j].match_gagne < participant[j+1].match_gagne:
                aux = participant[j+1]
                participant[j+1] = participant[j]
                participant[j] = aux
            elif participant[j].match_gagne == participant[j+1].match_gagne:
                if participant[j].match_egalite < participant[j+1].match_egalite:
                    aux = participant[j+1]
                    participant[j+1] = participant[j]
                    participant[j] = aux
                elif participant[j].match_egalite == participant[j+1].match_egalite:
                    if participant[j].combat_gagne < participant[j+1].combat_gagne:
                        aux = participant[j+1]
                        participant[j+1] = participant[j]
                        participant[j] = aux
                    elif participant[j].combat_gagne == participant[j+1].combat_gagne:
                        if participant[j].combat_egalite < participant[j+1].combat_egalite:
                            aux = participant[j+1]
                            participant[j+1] = participant[j]
                            participant[j] = aux
                        #Si les deux strategies ont exactement le meme nombre de victoire et d'egalite, alors ils sont ex aequo, on ne les intervertit pass
    resultat(participant)

def Combat(strat1, strat2, texte):
    if(texte=="-v" or texte=="-vv"):
        print(strat1.nom+ " "*10+ strat2.nom)
        print("Total points :", end="")
    gagnant = [0,0]
    for j in range(5):
        for i in range(200):
            strat1.choix(strat2.prec_coup)
            strat2.choix(strat1.prec_coup)

            point = Table_gain["I"+strat1.coup+"J"+strat2.coup]
            strat1.point += point[0]
            strat2.point += point[1]

            if(j == 0 and texte=="-vv"):
                affiche_coup(strat1, strat2)

            strat1.prec_coup = strat1.coup
            strat2.prec_coup = strat2.coup

        if strat1.point > strat2.point:
            gagnant[0] += 1
            strat1.combat_gagne += 1
            strat2.combat_perdu += 1
            
        elif strat1.point < strat2.point:
            gagnant[1] += 1
            strat2.combat_gagne += 1
            strat1.combat_perdu += 1
        else:
            strat2.combat_egalite += 1
            strat1.combat_egalite += 1
        if(texte=="-v" or texte=="-vv"):
            print(str(strat1.point) + "--" + str(strat2.point) + "    ", end = "")
        strat1.reinitialisation()
        strat2.reinitialisation()
    if(texte=="-v" or texte=="-vv"):
        print("")
        print("Gagnant : ",end = "")
    if(gagnant[0]>gagnant[1]) :
        strat1.match_gagne += 1
        strat2.match_perdu += 1
        if(texte == "-v"):
            print(strat1.nom)
    elif(gagnant[0]<gagnant[1]):
        if(texte=="-v" or texte=="-vv"):
            print(strat2.nom)
        strat2.match_gagne += 1
        strat1.match_perdu += 1
    else:
        if(texte=="-v" or texte=="-vv"):
            print("Egalite")
        strat2.match_egalite += 1
        strat1.match_egalite += 1


def Tournoi(texte):
    participant = []
    for i in Strat:
        participant.append(s.Strategie(i))
    for i in range(len(participant)):
        for j in range(i+1, len(participant)):
            Combat(participant[i], participant[j], texte)
    classement(participant)
            
                
def main(texte):
    if(len(texte)==2):
        Tournoi(texte[1])
    elif(len(texte)>=3):
        if texte[1] in Strat:
            strat1 = s.Strategie(texte[1])
        else:
            print("Erreur dans l'entrée d'une strategie")
            return 0
        if texte[2] in Strat:
            strat2 = s.Strategie(texte[2])
        else:
            print("Erreur dans l'entrée d'une strategie")
            return 0
        if(len(texte)==4): 
            Combat(strat1, strat2, texte[3])
        else:
            Combat(strat1, strat2, "-v")
    else:
        Tournoi("")

main(sys.argv)
