grapheInitial = []
nbEtat = int(input("Saisir le nombre d'etat : "))


def getSuccesseurs(numeroEtat):
    tab = []
    for i in range(nbEtat):
        #Pour acceder au predesseur d'un etat il fau parcourir le tableau à partir de nbEtat*numeroEtat pendant nbEtat 
        if(grapheInitial[nbEtat*numeroEtat+i] == 1):
            #recupere le num de l'etat
            tab.append(i)
    return tab
def dejaTraite(i):
    for z in tabCouleur :
        if z[0] == i:
            return True
    return False
grapheInitial = [[0 for j in range(nbEtat)] for v in range(nbEtat)]
#Permet de renseigner les liens entre les différents etat
#Seu la moitié du tableau est a renseigner puisque l'on est dans un graphe non oriente, si il existe un lien de 0 a 1 alors il existe un lien de 1 a 0
for i in range(nbEtat):
  for y in range(i,nbEtat):
    choix = int(input("Graphe : Existe t il un lien entre "+str(i)+" et : "+str(y)+ " ?  1/0  :"))
    if i != y :    
      grapheInitial[i][y] = choix
      grapheInitial[y][i] = choix
    else:
      #Les liens d'un sommet vers lui meme sont inutiles pour la coloration de graphes
      grapheInitial[i][y] = 0
#Convertion un tableau 2d en 1d
#L utilisation d'un tableau 2d etait plus pratique dans ce cas
grapheInitial = list(sum(grapheInitial,[]))
tabEtatTrie = []
for i in range(0,nbEtat):
    tabEtatTrie.append([i,len(getSuccesseurs(i))])


#Trie du tableau selon le second element de chaque case qui corespond au nombre de succeseur
def takeSecond(elem):
    return elem[1]
tabEtatTrie.sort(key=takeSecond,reverse=True)
couleur = 1
tabCouleur = []
compteur = 0
while len(tabCouleur) < nbEtat:
    tabCouleur.append([tabEtatTrie[compteur][0],"Couleur"+str(couleur)])
    tmp = []
    for i in range(0,nbEtat):
        
        ok = True
        #Si l'element courant est adjacent a l'un des sommet possedant la couleur courante alors on ne realise pas la
        #condition suivantes(les element possedant la couleur courante se trouve dans tmp)
        for z in tmp:
            if i in getSuccesseurs(z):
                ok = False
        #Si i n'est pas adjacent au premier sommet non traite de la liste 
        if i not in getSuccesseurs(tabEtatTrie[compteur][0]) and i != tabEtatTrie[compteur][0] and dejaTraite(i)==False and ok == True:
            tabCouleur.append([i,"Couleur"+str(couleur)])
            tmp.append(i)
            ok = True
        if i == nbEtat-1:
            break
    #On change de couleur pour passer a un nouveau groupe d'etats
    couleur = couleur + 1
    compteur = compteur +1

print(tabCouleur)
