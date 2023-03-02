class Ville():
    def __init__(self, nom, nombre_habitant):
        self.nom = nom
        self.nombre_habitant = nombre_habitant

    def ajouterPopulation(self):
        self.population += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.age = age
        self.nom = nom
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.nombre_habitant += 1


paris = Ville("Paris", 1000000)
print("Population de la ville de Paris:", paris.nombre_habitant, "habitants")


marseille = Ville("Marseille", 861635)
print("Population de la ville de Marseille:",
      marseille.nombre_habitant, "habitants")

jhon = Personne("jhon", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloe", 18, marseille)

jhon.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print("Mise a jour de la population de la ville de Paris :",
      paris.nombre_habitant, "habitants")
print("Mise a jour de la population de la ville de Marseille :",
      marseille.nombre_habitant, "habitants")
