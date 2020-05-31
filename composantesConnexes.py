grapheInitial = []
nbEtat = int(input("Saisir le nombre d'etat : "))
oriente = input("Le graphe est il orienté ? : o/n ")

def getSuccesseurs(numeroEtat):
    tab = []
    for i in range(nbEtat):
        #Pour acceder au predesseur d'un etat il fau parcourir le tableau à partir de nbEtat*numeroEtat pendant nbEtat 
        if(grapheInitial[nbEtat*numeroEtat+i] == 1):
            #recupere le num de l'etat
            tab.append(i)
    return tab

#Puisqu'on utilise la reecusrivite, la liste doit etre declarer en global
elementtraite = []
#Permet de trouver les etat fortement connexe avec l'etat passé en parametre
def findCompConnexe(elem):
    #l'element est traité
    elementtraite.append(elem)
    #Pour un sommet on cherche les successeur
    listeSucesseur = getSuccesseurs(elem)
    #puis si un des sucesseur de elem a pour sucesseur elem alors il sont fortement connexe
    for sucesseur in listeSucesseur:     
        if elem in getSuccesseurs(sucesseur) :
            #Alors les deux sommet sont connexes
            grapheConnexe.append(sucesseur)
            grapheConnexe.append(elem)
            #Cette condition evite la boucle infini
            #Si un etat a deja été traité alors on ne le retraite pas
            if sucesseur not in elementtraite:
                elementtraite.append(sucesseur)
                #Pour chaque etat fortement connexe à l'etat initiale on cherche leur composant conexe et ainsi de suite
                findCompConnexe(sucesseur)


#dans le cas d un graphe oriente on renseigne tout les liens possible entre les sommets
if(oriente == "o"):            
    #Permet de renseigner les liens entre les différents etat
    for i in range(nbEtat):
        for y in range(nbEtat):
            choix = input("Graphe : Successeur "+str(i)+"     Prédécesseur : "+str(y)+ " ?  1/0  :")
            if i != y :    
                grapheInitial.append(int(choix))
            else:
                grapheInitial.append(0)
#Dans le cas d'un graphe non oriente on renseigne seulement la moitie du tableau par rapport à la diagonale. puisque si il existe un lien non oriente de 1 a 0 alors
#c'est comme si il existait un lien oriente de 1 à 0 et de 0 à 1
if(oriente == "n"):
    grapheInitial = [[0 for j in range(nbEtat)] for v in range(nbEtat)]
    #Permet de renseigner les liens entre les différents etat
    for i in range(nbEtat):
        for y in range(i,nbEtat):
            choix = int(input("Graphe : Existe t il un lien entre "+str(i)+" et : "+str(y)+ " ?  1/0  :"))
            if i != y :    
                grapheInitial[i][y] = choix
                grapheInitial[y][i] = choix
            else:
                #Les liens d'un sommet vers lui meme sont inutiles ici
                grapheInitial[i][y] = 0
    #Converti un tableau 2d en 1d
    #L utilisation d'un tableau 2d etait plus pratique dans ce cas
    grapheInitial = list(sum(grapheInitial,[]))    
#print(grapheInitial)
            
grapheConnexe = []
#pour chaque sommet du graphes
for y in range(nbEtat):
    #Si l'on a deja cherché les etats fortement connexes de l'etat en cours pas besoin de les re chercher
    if  y not in elementtraite:
        findCompConnexe(y)
        if len(grapheConnexe) > 0:
            #On affiche la liste en suprimant les doublon
            print("Nouvelle composante fortement connexe : ")
            print(list(dict.fromkeys(grapheConnexe)))
            #on vide la liste pusqu'elle resert après
            grapheConnexe = []

