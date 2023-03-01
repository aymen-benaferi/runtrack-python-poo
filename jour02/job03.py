class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a ete emprunte.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a ete rendu.")
        else:
            print("Le livre n'a pas ete emprunte.")


mon_livre = Livre("One piece", "Oda", 150)

print(mon_livre.verification())

mon_livre.emprunter()

print(mon_livre.verification())

mon_livre.emprunter()

mon_livre.rendre()

print(mon_livre.verification())
mon_livre.rendre()
