listeA = []
listeB = []
listeA1 = []
listeB1 = []
compteur = 0
nbEtat = int(input("Saisir le nombre d'etat : "))
print("L'etat initiale doit etre 0 ")
NouveauxEtat = []

#Si le tableau d numero d'etat passé en paramètre ne se trouve pas dan la liste des nouveau etats
def estNouveauEtat(tab):
    for i in range(len(NouveauxEtat)):
        if tab == NouveauxEtat[i]:

            return False
    return True

#Permet de récupérer la liste des succésseur à parti d'un symbole et d'un prédécésseur
def getSuccesseurs(symb,numeroEtat):
    tab = []
    if symb == "A":
        for i in range(nbEtat):
            #Pour acceder au predesseur d'un etat il fau parcourir le tableau à partir de nbEtat*numeroEtat pendant nbEtat 
            if(listeA[nbEtat*numeroEtat+i] == 1):
                #recupere le num de l'etat
                tab.append(i)
        return tab
    if symb == "B":
        for i in range(nbEtat):
            if(listeB[nbEtat*numeroEtat+i] == 1):
                #Recupere le num de l'etat
                tab.append(i)
        return tab
    
#Permet de renseigner les liens entre les différents etat
for i in range(nbEtat):
    for y in range(nbEtat):
        choix = input("A : Successeur "+str(i)+"     Prédécesseur : "+str(y)+ " ?  1/0  :")
        listeA.append(int(choix))
        
    for x in range(nbEtat):
        choix = input("B : Successeur"+str(i)+"     Prédécesseur : "+str(x)+ " ?  1/0  :")
        listeB.append(int(choix))
        
#Initialisation
etatFinal = int(input("Saisir l'état finale entre 0 et "+ str(nbEtat-1)+" "))
etatInitial = 0
NouveauxEtat.append([etatInitial])

#Traitements
z = 0
while True:
#for z in range(len(NouveauxEtat)):
    tableau1 = []
    tableau2 = []
    #On parcours chaque ancien etat du nouvelle état par exemple [0,1,2]-> 0,1,2
    for i in range(len(NouveauxEtat[z])):        
        tableau1.append(getSuccesseurs("A",NouveauxEtat[z][i]))
    for i in range(len(NouveauxEtat[z])):        
        tableau2.append(getSuccesseurs("B",NouveauxEtat[z][i]))
        #sum permet de passer d'un tableau 2D à 1D
        #set permet de retirer les doublons
        #list converti en list
    tableau1 = list(set(sum(tableau1,[])))
    tableau2 = list(set(sum(tableau2,[])))
    print("Nouveau super etat :"+str(NouveauxEtat[z]
                                     ))
    print("Successeur avec symbole 'A' : "+str(tableau1))
    print("Successeur avec symbole 'B' : "+str(tableau2))
    #Si c'est un nouvelle etat alors on le mets dans la liste des nouvelle etat
    if estNouveauEtat(tableau1):
        NouveauxEtat.append(tableau1)
    if estNouveauEtat(tableau2):
        NouveauxEtat.append(tableau2)
    #Si l'etat final se trouve dans un des nouveaux etat alors il est final aussi
    if etatFinal in NouveauxEtat[z]:
        print("Cet état est terminal ")
    if z == 0:
        print("Cet etat est initial ")
    print()
    #Si il n'y a plus de nouveaux état à traité alors on quitte la boucle sinon on passe au autre nouvelle etat
    if(z == len(NouveauxEtat)-1 ):
        break
    z += 1



    
