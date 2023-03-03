class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("bonjour")

    def allerEnCours(self):
        print("je vais en cours")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")



personne1 = Personne()
eleve1 = Eleve()


eleve1.afficherAge()
