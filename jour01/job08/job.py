class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True
        
    def get_titre(self):
        return self._titre
    
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre
    
    def get_auteur(self):
        return self._auteur
    
    def set_auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur
    
    def get_nb_pages(self):
        return self._nb_pages
    
    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self._nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
            
    def est_disponible(self):
        return self._disponible
    
    def emprunter(self):
        if self.est_disponible():
            self._disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
            
    def rendre(self):
        if not self.est_disponible():
            self._disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")
            
    def __str__(self):
        return f"{self._titre} par {self._auteur}, {self._nb_pages} pages"
mon_livre = Livre("Le Rouge et le Noir", "Stendhal", 512)

print(mon_livre.est_disponible())  # Affiche True
mon_livre.emprunter()  # Affiche "Le livre a été emprunté."
print(mon_livre.est_disponible())  # Affiche False
mon_livre.emprunter()  # Affiche "Le livre n'est pas disponible."
mon_livre.rendre()  # Affiche "Le livre a été rendu."
print(mon_livre.est_disponible())  # Affiche True
mon_livre.rendre()  # Affiche "Le livre n'a pas été emprunté."
