#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule le factoriel d'un entier positif."""
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n pour éviter une boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Le nombre doit être un entier positif.")
            sys.exit(1)
    except ValueError:
        print("L'argument doit être un entier valide.")
        sys.exit(1)

    f = factorial(number)
    print(f)
