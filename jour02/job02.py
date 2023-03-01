class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def et_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("erreur:le nombre de pages doit etre un entier positif.")


livre = Livre("One piece", "Oda", 150)

print(livre.get_auteur())
print(livre.get_nb_pages())

livre.set_nb_pages(-100)

print(livre.get_nb_pages())
