# -*- coding: utf-8 -*-
#A faire : moyenne de chaque gens

############################################################################################################################
#%% importation de module pour realiser le projet ##########################################################################
############################################################################################################################ 
import csv
import numpy as np
import sys


def stop():
    a=str(input("Souhaitez-vous continuer ? Oui : o, Non : "))
    if a == "o" :
        pass
    else : 
        sys.exit(0) 



print("Bonjour! Bienvenue sur notre plateforme interactive !")
a = str(input("Pour bien commencer, veuillez cliquer sur 'p' si vous connaissez déjà les fonctions existentes, sinon tapez 'c' :"))
if a == "c" :
    pass
elif a == "P" :
    print ("Voici les fonctions existantes : blabla")
stop()



############################################################################################################################
#%% Programme permettant de mettre les notes superieures au plafond ########################################################
############################################################################################################################
with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

entete = your_list.pop(0) #supprime la premiere ligne d'entete du tableau
T = np.array(your_list).astype(np.float) #transforme tous les elements du tableau (string) en float


############################################################################################################################
#%% Programme permettant de mettre les notes superieures au plafond ########################################################
############################################################################################################################
"""
for i in range (len(T)): #pour tous les i appartenant aÂ  l'intervalle [nombre d'elements du tableau T]
#si l'element est superieur aÂ  50, alors cet element prend comme valeur 50   
    if T[i,0] > 50 : 
        T[i,0]=50   

for i in range (len(T)):
    if T[i,1] > 100 :
        T[i,1]=100
        
for i in range (len(T)):
    if T[i,2] > 100 :
        T[i,2]=100

for i in range (len(T)):
    if T[i,3] > 200 :
        T[i,3]=200
        
#print(T)   
"""

def maj(T,o,n):
    for i in range (len(T)): #pour tous les i appartenant Ã  l'intervalle [nombre d'Ã©lÃ©ments du tableau T]
    #si l'Ã©lÃ©ment est supÃ©rieur Ã  50, alors cet Ã©lÃ©ment prend comme valeur 50   
        if T[i,n] > o[n] : 
            T[i,n]= o[n] 
    return T
    stop()
        
def maj_tout(T,o):
    n=0
    while n<len(o):
        T=maj(T,o,n)
        n+=1
    return T
    stop()

############################################################################################################################
#%% fonction permettant de terminer le major de chaque theme ###############################################################
############################################################################################################################
def major (l,n):
    a_trier = []
    for liste in l :
        a_trier.append([liste[n]])
    for i in range (len(a_trier)):
        a_trier[i].append(i)
    a_trier = sorted(a_trier)
    a_trier = a_trier[::-1]
    print(a_trier[1])
    stop()


############################################################################################################################
#%% Attribution de chaque ligne de notes a un eleve######################################################################### 
############################################################################################################################
P = ["Jean","Pierre","Michel","Andre","Philippe","Rene","Louis","Alain",\
     "Jacques","Bernard","Marcel","Daniel","Roger","Robert","Claude","Paul",\
     "Christian","Henri","Georges","Nicolas","Francois","Patrick","Gerard",\
     "Christophe","Joseph","Julien","Maurice","Laurent","Frederic","David",\
     "Stephane","Pascal","Sebastien","Alexandre","Thierry","Olivier","Thomas",\
     "Raymond","Antoine","Guy","Dominique","Charles","Didier","Marc","Vincent",\
     "Yves","Guillaume","Bruno","Serge","Maxime","Marie","Jeanne","Claude",\
     "Francoise","Monique","Catherine","Nathalie","Isabelle","Jacqueline",\
     "Anne","Sylvie","Martine","Madeleine","Nicole","Suzanne","Helene",\
     "Christine","Marguerite","Denise","Christiane","Yvonne","Louise",\
     "Valerie","Sophie","Dominique","Sandrine","Stephanie","Celine",\
     "Veronique","Chantal","Marcelle","Renee","Simone","Jeannine","Paulette",\
     "Julie","Annie","Patricia","Brigitte","Lucie","Camille","Lea","Alice",\
     "Aurelie","Laurence","Michele","Cecile","Therese","Colette","Virginie"]

"""
name = input("Entrez le nom de l'eleve dont vous voulez connaitre les notes : \n") #Association d'un eleve a ses notes d'UE. Merci Philippe :)
rang = -1
if name in P:
    rang = P.index(name)
    print(name,"a obtenu les notes",T[rang]) #Enlever la derniere colonne et ajouter des lignes pour savoir si l'eleve a valide son UE
else:
    print("Vous ne connaissez pas vos eleves ? :( Entrez le nom d'un de vos eleves")
 """   
    
 
def nametorang(name):
    if name in P:
        return P.index(name)
    else:
        return "Erreur"
        


    
#pas fini
def qui(T,P):
    for i in range (len(T)):
        ihih = P[i]
        eheh = T.index(ihih)
    return eheh
            

 
def fiche_eleve(name,T,c):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        moyenne = moy_eleve(name,T,c)
        print(name, rang, " : Les notes de cette eleve sont ",T[rang],", sa moyenne est de ",moyenne)
    else:
        print("Erreur")
    stop()
  
    
############################################################################################################################
#%% Quels élèves ont eu leur semestre ###################################################################################### 
############################################################################################################################     
    
def oui_ou_non(name,T):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        if T[rang,4] == 1.0:
            return True
        else :
            return False
    else:
        return None
 

       
def print_oui_ou_non(name,T):
    if oui_ou_non(name,T) == True :
        print(name, "a eu son semestre !")
    elif oui_ou_non(name,T) == False :
        print(name,"n'a pas eu son semestre, et doit passer les rattrapages ...")
    else :
        print("Erreur")
    stop()



def oui_ou_non_tous(P,T):
    r = []
    for i in range (len(l)):
        if oui_ou_non(names[i],l):
            r.append(names[i])
    return r


    
def print_oui_ou_non_tous(P,T):
    print(oui_ou_non_tous(P,T))
    stop()

############################################################################################################################
#%% Attribution de chaque ligne de notes a un eleve ########################################################################
############################################################################################################################
#moyennes = np.mean(T,0)[:4] #0 : Traitement des valeurs en ligne pour chaque colonne.
                                    #Garde les 4 premieres valeurs

    

############################################################################################################################
#%% Moyenne pour un theme colonne n ########################################################################################
############################################################################################################################
def moy_colonne(n):
    moy = np.mean(T,0)[n]
    print("La moyenne de cette UE est de",moy)
    stop()
    
############################################################################################################################   
#%% Moyenne de chaque eleve ################################################################################################
############################################################################################################################ 
def moy_eleve(name,T,c):  #e : numéro de ligne du tableau et c : Coefficient ici 9
    m=0
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        for i in range(len(T[rang])):
            m += T[rang][i]  #rang i dans la liste e (ligne du tableau) de la liste T
        m = m/c #On considère qu'une note sur 50 a un coefficient 1 dans notre cas actuel
        return m
    else:
        print("Erreur")
    stop()


############################################################################################################################   
#%% Courbe nb XP <=> note sur 20 ###########################################################################################
############################################################################################################################ 

import matplotlib.pyplot as plt
import numpy as np

AA = [3,8,16,25,36,48,62,78,94,112,131,151,172,194,218,243,267,294,321,350]
BB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def courbe_nbXP_note20(plafond):
    x=np.linspace(0,plafond+30,10)
    plt.plot(AA,BB)
    plt.ylabel('Nombre de XP')
    plt.xlabel("Note sur 20")
    plt.show()

#pas fini
def quelle_note?(XP,AA,BB):
    for i in AA:
        while AA[i] =< XP =< AA[i+1]:
            AA[i] = BB[i]
            AA[i+1] = BB[i+1]
            nXP = 
