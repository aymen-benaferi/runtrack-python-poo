def puissance(x, n):
    """
    Calcule x^n en utilisant la récursivité.
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = puissance(x, n/2)
        return y*y
    else:
        return x*puissance(x, n-1)


x = int(input("Entrez un nombre entier : "))
n = int(input("Entrez un autre nombre entier : "))
resultat = puissance(x, n)
print(f"{x}^{n} = {resultat}")
