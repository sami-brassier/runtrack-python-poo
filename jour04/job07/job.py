import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        if self.valeur in ["J", "Q", "K"]:
            return 10
        elif self.valeur == "A":
            return 11
        else:
            return int(self.valeur)
        
class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ["Coeur", "Carreau", "Trèfle", "Pique"]:
            for valeur in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)
    
    def donne_carte(self):
        return self.paquet.pop(0)
    
def jouer_blackjack():
    jeu = Jeu()
    joueur_main = [jeu.donne_carte(), jeu.donne_carte()]
    croupier_main = [jeu.donne_carte(), jeu.donne_carte()]
    
    print(f"Joueur: {joueur_main[0]}, {joueur_main[1]}")
    print(f"Croupier: {croupier_main[0]}, *")
    
    joueur_pts = sum([carte.get_valeur() for carte in joueur_main])
    croupier_pts = sum([carte.get_valeur() for carte in croupier_main])
    
    while True:
        choix = input("Voulez-vous prendre une carte? (o/n) ")
        if choix.lower() == "o":
            nouvelle_carte = jeu.donne_carte()
            print(f"Vous avez reçu la carte {nouvelle_carte}")
            joueur_main.append(nouvelle_carte)
            joueur_pts += nouvelle_carte.get_valeur()
            print(f"Joueur: {', '.join(map(str, joueur_main))} (total: {joueur_pts})")
            if joueur_pts > 21:
                print("Vous avez dépassé 21, vous avez perdu!")
                return
        else:
            break
    
    while croupier_pts < 17:
        nouvelle_carte = jeu.donne_carte()
        print(f"Le croupier a reçu la carte {nouvelle_carte}")
        croupier_main.append(nouvelle_carte)
        croupier_pts += nouvelle_carte.get_valeur()
        print(f"Croupier: {', '.join(map(str, croupier_main))} (total: {croupier_pts})")
        if croupier_pts > 21:
            print("Le croupier a dépassé 21, vous avez gagné!")
            return
    
    if joueur_pts > croupier_pts:
        print("Vous avez gagné!")
    elif joueur_pts == croupier_pts:
        print("Égalité!")
    else:
        print("Le croupier a gagné!")

jouer_blackjack()