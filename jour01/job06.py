class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print("L'animal se nomme", self.prenom)


animal = Animal()
print(animal.age)


animal.vieillir()
print(animal.age)

animal = Animal()
animal.nommer("Luna")
