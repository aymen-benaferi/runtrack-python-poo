class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(
            f"Produit : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA


p1 = Produit("Souris", 30, 20)
p2 = Produit("Clavier", 50, 20)
p3 = Produit("Ecran", 200, 20)

print(p1.calculerPrixTTC())
print(p2.calculerPrixTTC())
print(p3.calculerPrixTTC())

p1.afficher()
p2.afficher()
p3.afficher()

p1.modifierNom("souris")
p1.modifierPrixHT(30)

p2.modifierNom("clavier")
p2.modifierPrixHT(50)

p3.modifierNom("Ecran")
p3.modifierPrixHT(200)
