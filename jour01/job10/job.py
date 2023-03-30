class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.en_marche = True
            print("La voiture a démarré.")
        else:
            print("Le réservoir est presque vide, il faut faire le plein.")

    def arreter(self):
        self.en_marche = False
        print("La voiture a été arrêtée.")

    def verifier_plein(self):
        return self.reservoir

# Exemple d'utilisation
voiture1 = Voiture("Peugeot", "308", 2010, 100000)
voiture1.demarrer()  # Affiche "La voiture a démarré."
voiture1.arreter()  # Affiche "La voiture a été arrêtée."
