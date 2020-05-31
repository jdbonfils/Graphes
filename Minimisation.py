import sys
listeA = []
listeB = []

compteur = 0
nbEtat = int(input("Saisir le nombre d'etat : "))
print("L'etat initiale doit etre 0 ")
NouveauxEtat = []
#Oulogique de taille 1

def OULogique(bin1,bin2):
    if bin1 == 1 or bin2 == 1:
        return 1
    else:
        return 0

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
            #Pour acceder au successeur d'un etat il fau parcourir le tableau à partir de nbEtat*numeroEtat pendant nbEtat 
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
def getPredecesseur(symb,numeroEtat):
    tab = []
    if symb == "A":
        for i in range(nbEtat):
            if(listeA[numeroEtat+(i*nbEtat)] == 1):
                #recupere le num de l'etat
                tab.append(i)
        return tab
    if symb == "B":
        for i in range(nbEtat):
            if(listeB[numeroEtat*i] == 1):
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
pileEtatNDistingue = []
for i in range(nbEtat):
    if i != etatFinal:
        pileEtatNDistingue.append([i,etatFinal])
#Traitement de la pile

y = 0
while True:
        tabA1 = []
        tabA2 = []
        tabB1 = []
        tabB2 = []
        tabA1 = getPredecesseur("A",pileEtatNDistingue[y][0])
        tabA2 = getPredecesseur("A",pileEtatNDistingue[y][1])
        if len(tabA1)>0 and len(tabA2)>0:
            #Alors on empile si le couple n'existe pas deja
            for x in range(len(tabA1)):
                for z in range(len(tabA2)):
                    #on regarde si le couple x,y existe dans la pile
                    if [x,z] not in pileEtatNDistingue:
                        pileEtatNDistingue.append([x,z])
                   
        tabB1 = getPredecesseur("B",pileEtatNDistingue[y][0])
        tabB2 = getPredecesseur("B",pileEtatNDistingue[y][1])
        if len(tabA1)>0 and len(tabA2)>0:
            #Alors on empile si le couple n'existe pas deja
            for x in range(len(tabA1)):
                for z in range(len(tabA2)):
                    #on regarde si le couple x,y existe dans la pile
                    if[x,z] not in pileEtatNDistingue:
                        pileEtatNDistingue.append([x,z])
        #On quitte la boucle si il n'ya plus d'etat à traité
        if y == len(pileEtatNDistingue)-1:
            break
        y += 1

EtatReunis = []   
#Recherche de couple distingué
trouve = False
for p in range(nbEtat):
    for q in range(nbEtat):
        for w in pileEtatNDistingue:
            #Le couple 1,2 est equivalent au couple 2,1
            if w == [p,q] or w ==[q,p]:
                trouve = True
        #Si le couple p q n'est pas dans la pile des etat alors ils doivent etre reunis
        if trouve == False:
            if p != q:
                #Ne rajoute pas le couple si il y est deja dans la liste
                if [p,q] not in EtatReunis and [q,p] not in EtatReunis:
                    EtatReunis.append([p,q])
            
        trouve = False

#Reunions des couples
nouvListeA = []
nouvListeB = []
if len(EtatReunis) != 0:
    for i in range(len(EtatReunis)):
        for y in range(len(EtatReunis[i])):
            for z in range(nbEtat):
                nouvListeA.append(listeA[EtatReunis[i][y]*nbEtat+z])
                nouvListeB.append(listeB[EtatReunis[i][y]*nbEtat+z])
else:
    print("Impossible de plus minimiser cet automate")
    #On arrete le programme
    
    sys.exit()
#Ou logique entre les couples
tabA = []
tabB = []
for i in range(nbEtat):
    tabA.append(OULogique(nouvListeA[i],nouvListeA[i+nbEtat]))
    tabB.append(OULogique(nouvListeB[i],nouvListeB[i+nbEtat]))
#Affichage des nouveaux super etats
for i in range(len(EtatReunis)):
    print("Nouveau Super Etat : ")
    print(EtatReunis[i])
    if 0 in EtatReunis[i]:
        print("Cet etat est initial ")
    if etatFinal in EtatReunis[i]:
        print("Cet etat est final ")
    

    for y in range(nbEtat):
        if tabA[y] == 1:
            if y in EtatReunis[i]:
                 print(" Successeur en A :"+str(EtatReunis[i]))
            else:
                 print(" Successeur en A :"+str(y))
        if tabB[y] == 1:
            if y in EtatReunis[i]:
                 print(" Successeur en B :"+str(EtatReunis[i]))
            else:
                 print(" Successeur en B :"+str(y))
        
        



    
            
        



            
