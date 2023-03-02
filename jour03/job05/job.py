import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        degats = random.randint(1, 10)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} points de dégâts !")

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        while self.niveau not in ["facile", "moyen", "difficile"]:
            self.niveau = input("Choisissez le niveau de difficulté (facile, moyen, difficile) : ")

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == "facile":
            joueur = Personnage("Joueur", 50)
            ennemi = Personnage("Ennemi", 30)
        elif self.niveau == "moyen":
            joueur = Personnage("Joueur", 40)
            ennemi = Personnage("Ennemi", 40)
        else:
            joueur = Personnage("Joueur", 30)
            ennemi = Personnage("Ennemi", 50)

        print(f"Un ennemi apparaît ! Vous devez le vaincre !\n")
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)
            self.verifierSante(joueur, ennemi)

        if joueur.vie > 0:
            print("Vous avez vaincu l'ennemi !")
        else:
            print("Vous avez été vaincu...")

    def verifierSante(self, joueur, ennemi):
        print(f"\nSanté de {joueur.nom} : {joueur.vie}")
        print(f"Santé de {ennemi.nom} : {ennemi.vie}\n")

# Exemple d'utilisation
jeu = Jeu()
jeu.lancerJeu()
