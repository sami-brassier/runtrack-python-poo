class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Numéro de compte:", self.__numero)
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Solde:", self.__solde)
        print("Autorisation de découvert:", self.__decouvert)

    def afficherSolde(self):
        print("Le solde du compte est de", self.__solde)

    def versement(self, montant):
        self.__solde += montant
        print("Versement de", montant, "euros effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible: le solde est insuffisant.")
        else:
            self.__solde -= montant
            print("Retrait de", montant, "euros effectué.")
            self.afficherSolde()

    def agios(self, taux):
        if self.__solde < 0:
            self.__solde *= (1 + taux)
            print("Des agios ont été appliqués.")
        else:
            print("Le solde est positif, pas d'agios à appliquer.")

    def virement(self, compte_dest, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible: le solde est insuffisant.")
        else:
            self.__solde -= montant
            compte_dest.versement(montant)
            print("Virement de", montant, "euros effectué vers le compte", compte_dest.__numero)

compte1 = CompteBancaire("123456", "Dupont", "Jean", 1000, True)

compte1.afficher()

compte1.versement(500)

compte1.retrait(200)

compte1.retrait(1000)

compte1.agios(0.05)

compte2 = CompteBancaire("789012", "Durand", "Alice", -500, True)

compte1.virement(compte2, 400)