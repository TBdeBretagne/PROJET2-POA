class Strategie:
    def __init__():
        nom = "" # parmis "All-D", "Random", "Tit-for-tat", "Tester", "Joss"
        coup = "" # prochain coup
        prec_coup = "" #coup precedent
        indice = 0
        test = True

    def choix(prec_adversaire):
         match nom:
            case "All-D" :
                coup = "D"
            case "Random":
                coup = random.choice("C","D")
            case "Tit-for-tat":
                if prec_adversaire == "" or test:
                    test = False
                    coup = "C"
                else:
                    coup = prec_adversaire
            case "Tester":
                if prec_adversaire == "":
                    coup = "D"
                elif test and prec_adversaire == "D":
                    coup = "D"
                    nom = "Tit-for-tat"
                else:
                    test = False
                    if indice == 2:
                        coup = "D"
                    else:
                        coup = "C"
                     indice = (indice + 1) % 3
            case "Joss":
                if prec_adversaire == "":
                    coup = "C"
                else:
                    if indice == 0:
                        coup = "D"
                    else:
                        coup = prec_adversaire

                indice = (indice + 1) % 10
                


           
                    
