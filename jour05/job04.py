def plus_grand_chiffre(liste):
    """
    Trouve le plus grand chiffre de la liste en utilisant la récursivité.
    """
    if len(liste) == 1:
        return liste[0]
    else:
        x = plus_grand_chiffre(liste[1:])
        return liste[0] if liste[0] > x else x


liste = [5, 6, 4, 2, 1, 8, 7]
resultat = plus_grand_chiffre(liste)
print(f"Le plus grand chiffre de la liste {liste} est {resultat}.")
