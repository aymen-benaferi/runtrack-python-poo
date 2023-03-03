class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print("Bonjour, je m'appelle", self.nom)


class Eleve(Personne):
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def allerEnCours(self):
        print("Je vais en cours")


class Professeur(Personne):
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def enseigner(self):
        print("Le cours va commencer")


eleve = Eleve("aymen", 15)
eleve.bonjour()
eleve.allerEnCours()

professeur = Professeur("sylvie", 40)
professeur.bonjour()
professeur.enseigner()
