def longueur(chaine):
    """
    Calcule la longueur de la chaîne de caractères en utilisant la récursivité.
    """
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])


chaine = input("entre une chaine de caracteres : ")
resultat = longueur(chaine)
print(f"La chaîne '{chaine}' a une longueur de {resultat}.")
