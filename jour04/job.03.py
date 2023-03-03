class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


r = Rectangle(10, 6)
print("longueur : ", r.get_longueur())
print("largeur : ", r.get_largeur())
print("perimetre : ", r.perimetre())
print("surface : ", r.surface())

p = Parallelepipede(10, 8, 6)
print("longueur : ", p.get_longueur())
print("largeur : ", p.get_largeur())
print("hauteur : ", p.get_hauteur())
print("perimetre : ", p.perimetre())
print("surface : ", p.surface())
print("volume : ", p.volume())
