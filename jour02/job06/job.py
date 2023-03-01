class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en cours"
        self.__total = 0

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats[nom_plat] = {"prix": prix_plat, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"
        self.__plats = {}

    def __calculer_total(self):
        self.__total = sum([plat["prix"] for plat in self.__plats.values()])

    def afficher_commande(self):
        self.__calculer_total()
        print("Commande n°{}:".format(self.__num_commande))
        for nom_plat, plat in self.__plats.items():
            print("- {} ({}) : {:.2f}€".format(nom_plat, plat["statut"], plat["prix"]))
        print("Total : {:.2f}€".format(self.__total))

    def calculer_tva(self, taux_tva):
        self.__calculer_total()
        tva = self.__total * taux_tva
        return tva

commande1 = Commande(1)

commande1.ajouter_plat("Pizza", 12.50)
commande1.ajouter_plat("Salade", 8.90)
commande1.ajouter_plat("Tiramisu", 5.50)

commande1.afficher_commande()

tva = commande1.calculer_tva(0.20)
print("TVA : {:.2f}€".format(tva))

commande1.annuler_commande()
