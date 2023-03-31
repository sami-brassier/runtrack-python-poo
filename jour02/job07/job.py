import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ['Coeur', 'Carreau', 'Pique', 'Trèfle']:
            for valeur in range(2, 11):
                self.paquet.append(Carte(valeur, couleur))
            for valeur in ['Valet', 'Dame', 'Roi']:
                self.paquet.append(Carte(10, couleur))
            self.paquet.append(Carte(1, couleur))
            self.paquet.append(Carte(11, couleur))

    def tirer_carte(self):
        return self.paquet.pop(random.randint(0, len(self.paquet)-1))

def jeu_blackjack():
    # Initialisation du jeu
    jeu = Jeu()
    random.shuffle(jeu.paquet)

    # Distribution des cartes
    joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
    croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

    # Tour du joueur
    while sum([carte.valeur for carte in joueur]) < 21:
        print('Joueur :', [carte.valeur for carte in joueur])
        choix = input('Voulez-vous tirer une carte ? (Oui/Non) ')
        if choix.lower() == 'oui':
            joueur.append(jeu.tirer_carte())
        else:
            break

    # Tour du croupier
    while sum([carte.valeur for carte in croupier]) < 17:
        croupier.append(jeu.tirer_carte())

    # Résultat
    print('Joueur :', [carte.valeur for carte in joueur])
    print('Croupier :', [carte.valeur for carte in croupier])
    if sum([carte.valeur for carte in joueur]) > 21:
        print('Le joueur a perdu.')
    elif sum([carte.valeur for carte in joueur]) > sum([carte.valeur for carte in croupier]):
        print('Le joueur a gagné.')
    else:
        print('Le croupier a gagné.')

jeu_blackjack()
