class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats[nom_plat] = {"prix": prix_plat, "statut": "en cours"}

    def annuler(self):
        self.__statut = "annuler"
        for plat in self.__plats.values():
            plat["statut"] = "annuler"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats.values():
            if plat["statut"] != "annuler":
                total += plat["prix"]
        return total

    def afficher_commande(self):
        print("Commande n {}".format(self.__num_commande))
        for nom_plat, plat in self.__plats.items():
            print("- {} : {}  ({})".format(nom_plat,
                  plat["prix"], plat["statut"]))
        total = self.__calculer_total()
        print("Total : {} ".format(total))

    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.2
        return tva


commande1 = Commande(1)
commande1.ajouter_plat("pizza", 7)
commande1.ajouter_plat("tacos", 10)
commande1.ajouter_plat("sandwich", 4)

commande1.afficher_commande()


commande1.annuler()
commande1.afficher_commande()


tva = commande1.calculer_tva()
print("TVA : {} ".format(tva))
