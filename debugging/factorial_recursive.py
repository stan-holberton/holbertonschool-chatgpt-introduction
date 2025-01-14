#!/usr/bin/python3
import sys

# Fonction : factorial
# Description : Cette fonction calcule le factoriel d'un nombre entier n
# en utilisant une approche récursive.
# Paramètres : 
#    n (int) : Un entier pour lequel le factoriel doit être calculé.
# Retourne : 
#    int : Le factoriel de n, c'est-à-dire le produit des entiers de 1 à n.
def factorial(n):
    if n == 0:
        return 1  # Le factoriel de 0 est défini comme 1
    else:
        return n * factorial(n-1)  # Appel récursif pour calculer le factoriel

f = factorial(int(sys.argv[1]))  # Appel de la fonction avec l'argument de la ligne de commande
print(f)  # Affichage du résultat
