class Tache:
    def __init__(self, titre, description, statut="a faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminee"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


tache1 = Tache("faire les courses", "acheter du pain ")
tache2 = Tache("Faire le menage", "ranger la chambre")
tache3 = Tache("Ranger la chambre", "nettoyer les vitre de la chambre")


liste = ListeDeTaches()


liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)


print("Toutes les taches :")
liste.afficherListe()

print("Taches a faire :")
taches_a_faire = liste.filterListe("a faire")
for tache in taches_a_faire:
    print(tache)


print("Tache termine :")
liste.marquerCommeFinie(tache1)
print(tache1)


print("Tache supprimer:")
liste.supprimerTache(tache2)
liste.afficherListe()
