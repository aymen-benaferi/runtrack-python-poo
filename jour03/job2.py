class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde

    def afficher(self):
        print("Compte bancaire numero {} de {} {}".format(
            self.__numero_compte, self.__prenom, self.__nom))

    def afficherSolde(self):
        print("Le solde du compte est de {} euros".format(self.__solde))

    def versement(self, montant):
        self.__solde += montant
        print("Versement de {} euros effectuer. Nouveau solde : {} euros".format(
            montant, self.__solde))

    def retrait(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
            print("Retrait de {} euros effectuer. Nouveau solde : {} euros".format(
                montant, self.__solde))
        else:
            print("Le compte n'a pas suffisamment de fonds pour effectuer ce retrait.")


compte1 = CompteBancaire("0123456789", "Durand", "Jean", 1000)

compte1.afficher()

compte1.afficherSolde()

compte1.versement(500)

compte1.retrait(200)

compte1.retrait(2000)
