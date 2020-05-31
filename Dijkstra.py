grapheInitial = []
nbEtat = int(input("Saisir le nombre d'etat : "))
depart = int(input("Sommet de départ (saisir val entre 0 et "+str(nbEtat-1)+" ) : "))
arrivee = int(input("Sommet d'arrivee(saisir val entre 0 et "+str(nbEtat-1)+" ) : "))

#Permet de recuperer les successeurs d'un etat
def getSuccesseurs(numeroEtat):
    tab = []
    for i in range(nbEtat):
        #Pour acceder au predesseur d'un etat il fau parcourir le tableau à partir de nbEtat*numeroEtat pendant nbEtat 
        if(grapheInitial[nbEtat*numeroEtat+i] >= 0):
            #recupere le num de l'etat
            tab.append([i,grapheInitial[nbEtat*numeroEtat+i]])
    return tab

#On initialise le tableau de 0 de taille nbEtat constitue de nbEtat case
grapheInitial = [[0 for j in range(nbEtat)] for v in range(nbEtat)]
#Permet de renseigner les liens entre les différents etat
for i in range(nbEtat):
  for y in range(i,nbEtat):
    choix = int(input("Poids du lien entre "+str(i)+" et : "+str(y)+ " ?  Si le lien n'existe pas alors saisir -1  :"))
    if i != y :    
      grapheInitial[i][y] = choix
      grapheInitial[y][i] = choix
    else:
      #Les liens d'un sommet vers lui meme sont inutiles ici
      grapheInitial[i][y] = -1
#Converti un tableau 2d en 1d
#L utilisation d'un tableau 2d etait plus pratique dans ce cas
grapheInitial = list(sum(grapheInitial,[]))
plusCourtchemin = [[ "" for j in range(nbEtat)] for v in range(nbEtat)]


#Traitement

#On initialise le tableau avec -1 dans chaque case, ce tableau permet d'obtenir la distance minimal pour chaque etat par rapport à l'état de Depart
#Si la distance est -1 alors la distnce minimale est inconnue
listeDistDepart = [ -1 for j in range(nbEtat*nbEtat)]
#On recupere la liste des successeur du point de depart
listSucesseur = getSuccesseurs(depart)
etatVisite = []
#On ajoute l'etat de depart à la liste des etats visites
etatVisite.append(depart)
#On ajoute dans le tableau les distances du point de départ a chaque sucesseur
for i in range(0,len(listSucesseur)):
        listeDistDepart[(nbEtat*depart)+listSucesseur[i][0]] = listSucesseur[i][1]
#On cherche le plus petit chemin
plusPetitChemin = 100000 ;
for i in listeDistDepart:
    if i < plusPetitChemin and i > 0:
        plusPetitChemin = i
#On recupere le point le plus proche grace a la distance la plus proche
pointplusproche = (listeDistDepart.index(plusPetitChemin)) %nbEtat  
etatVisite.append(pointplusproche)

#Puis tant que l'etat d'arrive n'a pas ete visité on répete le code precedent
while arrivee not in etatVisite :
    #On cherche le point le plus proche
    etatVisite.append(pointplusproche)
    #On recupere les sucesseur du poin
    tabSucesseurs = getSuccesseurs(pointplusproche)
    #Pour chacun des successeurs du point on rajoute le poids du point de depart a ce point
    for i in range(0,len(tabSucesseurs)):
        tabSucesseurs[i][1] = tabSucesseurs[i][1]+plusPetitChemin
    for i in range(0,len(tabSucesseurs)):
        listeDistDepart[(nbEtat*pointplusproche)+tabSucesseurs[i][0]] = tabSucesseurs[i][1]
    #Condition de sortie des que l'état d'arrive est traité
    print(etatVisite)
    if arrivee in etatVisite :
        break
    #On cherche le plus petit chemin
    plusPetitChemin = 100000        
    for i in range(0,nbEtat*nbEtat):
        if (i%nbEtat) not in etatVisite:
            if listeDistDepart[i] < plusPetitChemin and listeDistDepart[i] > 0:
                plusPetitChemin = listeDistDepart[i]
                pointplusproche = i%nbEtat
                
#On affiche le poinds du plus petit chemin de depart a  arrivee
print("Le plus petit chemin est de taille : "+str(plusPetitChemin))
print("Chemin le plus court : ")
plusPetitChemin = 10000
#De arrive a depart on affiche le chemin le plus court
print("Etat :"+str(arrivee))
while arrivee != depart:
    for i in range (0,nbEtat):
        if listeDistDepart[arrivee+(nbEtat*i)] < plusPetitChemin and listeDistDepart[arrivee+(nbEtat*i)] > 0:
                plusPetitChemin = listeDistDepart[arrivee+(nbEtat*i)]
                tmp = i
    arrivee = tmp
    print("↓")
    print("Etat :"+str(arrivee))
    
    
