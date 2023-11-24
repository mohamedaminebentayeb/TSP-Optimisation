
import sys
import copy
import math
import time
import numpy as np
A =[[0,3,5,48,48,8,8,5,5,3,3,0,3],
[3,0,3,48,48,8,8,5,5,0,0,3,0],
[5,3,0,72,72,48,48,24,24,3,3,5,3],
[48,48,74,0,0,6,6,12,12,48,48,48,48],
[48,48,74,0,0,6,6,12,12,48,48,48,48],
[8,8,50,6,6,0,0,8,8,8,8,8,8],
[8,8,50,6,6,0,0,8,8,8,8,8,8],
[5,5,26,12,12,8,8,0,0,5,5,5,5],
[5,5,26,12,12,8,8,0,0,5,5,5,5],
[3,0,3,48,48,8,8,5,5,0,0,3,0],
[3,0,3,48,48,8,8,5,5,0,0,3,0],
[0,3,5,48,48,8,8,5,5,3,3,0,3],
[3,0,3,48,48,8,8,5,5,0,0,3,0],
]
# mettre les 0 (routes qui n'existe pas) avec une valeur du cout  infini
A = [[math.inf if x == 0 else x for x in row] for row in A]
# obtenir la taille de notre probléme
n = len(A[0])

# initialiser le dictionnaire g
memoire = {}

# initialiser la liste p pour stocker les chemins optimaux
stock= []


def TSP_DYNAMIC():
    # temps de début d'exécution
    start_time=time.time()
    #initialisation de la matrice 
    for x in range(1, n):
        memoire[x + 1, ()] = A[x][0]
        
    # On trouve la solution optimale
    result = get_solution_min(1, (2,3,4,5,6,7,8,9,10,11,12,13))
    
    # temps de fin d'exécution
    end_time=time.time()

    # temps d'exécution
    elapsed_time = end_time - start_time
    
    # On récupère la solution optimale
    solution = stock.pop()
    
    # On affiche le chemin optimal
    print('\n le plus court hemin est :  0 -> ', end='')
    print(solution[1][0]-1, end=', ')
    for x in range(n - 2):
        for new_solution in stock:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0]-1, end=' -> ')
                break
    print("0 avec un cout de ", result )
    print(" Temps d'exécution : ", elapsed_time)
    return


def get_solution_min(k, a):
    # Si cette solution a déjà été calculée, on retourne le résultat
    if (k, a) in memoire:
        return memoire[k, a]

    # On initialise deux listes vides pour stocker les valeurs et les solutions possibles
    valeurs = []
    all_min = []

    # On boucle sur chaque élément de l'ensemble a
    for j in a:
        # On crée une copie de l'ensemble a pour le modifier sans altérer l'original
        set_a = copy.deepcopy(list(a))
        # On retire l'élément j de l'ensemble pour le traiter comme point de départ suivant
        set_a.remove(j)
        # On stocke les solutions possibles sous forme de tuples (point j, ensemble restant)
        all_min.append([j, tuple(set_a)])
        # On appelle récursivement la fonction pour calculer la solution optimale de l'ensemble restant
        result = get_solution_min(j, tuple(set_a))
        # On ajoute le coût de l'arc entre les points k et j au coût de la solution optimale de l'ensemble restant
        valeurs.append(A[k-1][j-1] + result)
       

    # On choisit la solution optimale avec le coût minimal
    memoire[k, a] = min(valeurs)
    # On ajoute cette solution optimale et ses éléments (point j et ensemble restant) à la liste p
    stock.append(((k, a), all_min[valeurs.index(memoire[k, a])]))

    # On retourne le coût optimal de la solution pour l'ensemble a
    return memoire[k, a]





TSP_DYNAMIC()
