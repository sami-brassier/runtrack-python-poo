class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
        
    def marquerUnBut(self):
        self.buts_marques += 1
        
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        
    def afficherStatistiques(self):
        print(f"Statistiques pour le joueur {self.nom} (#{self.numero}, {self.position}) :")
        print(f"- Buts marqués : {self.buts_marques}")
        print(f"- Passes décisives effectuées : {self.passes_decisives}")
        print(f"- Cartons jaunes reçus : {self.cartons_jaunes}")
        print(f"- Cartons rouges reçus : {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques pour l'équipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
            
    def mettreAJourStatistiquesJoueur(self, numero_joueur, type_statistique):
        for joueur in self.joueurs:
            if joueur.numero == numero_joueur:
                if type_statistique == "but":
                    joueur.marquerUnBut()
                elif type_statistique == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif type_statistique == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif type_statistique == "rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Type de statistique invalide.")
                return
        print(f"Aucun joueur avec le numéro {numero_joueur} n'a été trouvé dans l'équipe.")

j1 = Joueur("Lionel Messi", 10, "attaquant")
j2 = Joueur("Cristiano Ronaldo", 7, "attaquant")
j3 = Joueur("N'Golo Kanté", 6, "milieu")

e1 = Equipe("FC Barcelone")
e2 = Equipe("Real Madrid")

e1.ajouterJoueur(j1)
e2.ajouterJoueur(j2)
e2.ajouterJoueur(j3)

e1.afficherStatistiquesJoueurs()
e2.afficherStatistiquesJoueurs()

e1.mettreAJourStatistiquesJoueur(10, "but")
e1.mettreAJourStatistiquesJoueur(10, "jaune")

e1.afficherStatistiquesJoueurs()
e2.afficherStatistiquesJoueurs()

e2.mettreAJourStatistiquesJoueur(6, "rouge")

e1.afficherStatistiquesJoueurs()
e2.afficherStatistiquesJoueurs()