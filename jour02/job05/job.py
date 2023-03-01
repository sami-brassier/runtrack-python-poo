class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50

    def set_marque(self, marque):
        self.marque = marque

    def set_modele(self, modele):
        self.modele = modele

    def set_annee(self, annee):
        self.annee = annee

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.reservoir = reservoir

    def get_marque(self):
        return self.marque

    def get_modele(self):
        return self.modele

    def get_annee(self):
        return self.annee

    def get_kilometrage(self):
        return self.kilometrage

    def get_en_marche(self):
        return self.en_marche

    def get_reservoir(self):
        return self.reservoir

    def demarrer(self):
        if self.verifier_plein():
            self.en_marche = True

    def arreter(self):
        self.en_marche = False

    def verifier_plein(self):
        if self.reservoir > 5:
            return True
        else:
            return False

ma_voiture = Voiture("Renault", "Clio", 2015, 50000)
ma_voiture.set_marque("Peugeot")
marque = ma_voiture.get_marque()
ma_voiture.demarrer()
ma_voiture.arreter()