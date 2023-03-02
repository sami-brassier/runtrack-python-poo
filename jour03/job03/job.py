class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
        
class ListeDeTaches:
    def __init__(self):
        self.taches = []
        
    def ajouterTache(self, tache):
        self.taches.append(tache)
        
    def supprimerTache(self, tache):
        self.taches.remove(tache)
        
    def marquerCommeFinie(self, tache):
        tache.statut = "terminé"
        
    def afficherListe(self):
        for tache in self.taches:
            print(tache.titre + " - " + tache.description + " - " + tache.statut)
            
    def filterListe(self, statut):
        taches_filtrees = []
        for tache in self.taches:
            if tache.statut == statut:
                taches_filtrees.append(tache)
        return taches_filtrees

tache1 = Tache("Tache 1", "Description tache 1")
tache2 = Tache("Regardez un film", "aller regarder un film sur la télévision")
tache3 = Tache("Appeler le médecin", "prendre rendez vous pour la semaine prochaine")

liste_de_taches = ListeDeTaches()

liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)
liste_de_taches.ajouterTache(tache3)

liste_de_taches.afficherListe()

liste_de_taches.marquerCommeFinie(tache1)

taches_a_faire = liste_de_taches.filterListe("à faire")
for tache in taches_a_faire:
    print(tache.titre + " - " + tache.description)

liste_de_taches.supprimerTache(tache3)

liste_de_taches.afficherListe()