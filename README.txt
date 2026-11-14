python3 main.py 	va lancer le tournoi entre tout les participants et afficher que le classements final avec le nombre de victoire, défaite et égalité de chaque stratégie.

Les paramètres suivant :
-v : va afficher le score final de chaque match, avec le détails de chaque combats , et le gagnant de chaque match.
-vv : va afficher en plus tout les coups de chaque combats.
b : va appliquer la modification du tournoi du bruit de 5\%. 
h : va appliquer la modification du tournoi de l'horizon inconnu, avec 1 chance sur 5 d'ajouter un nouveau rounds à chaque fois.

Pour le b et le h, du moment qu'ils sont présent, cela fonctionnera. écrire "bbbbaaahhh" activera les deux options. 
ce n'est pas restrictif aux caractères "b" et "h". Par contre, les options -v et -vv doivent commencer par ces caractères bien précisément. Il suffit donc d'écrire "-vvbh" pour tout activer.

Il est également possible de lancer un seul match avec la commande :		python3 main.py stratégie1 strategie2
Il est également possible d'ajouter les paramètres du dessus pour appliquer les modifications dans les combats ou l'affichage sur ce seul match. 
Cela ne marche uniquement avec des startégies connus du programme, c'est à dire : "All-D", "Random", "Tit-for-tat", "Tester", "Joss", "Graduale", "Spiteful"