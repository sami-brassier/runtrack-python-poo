class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        
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
            
    def __str__(self):
        return f"{self._titre} par {self._auteur}, {self._nb_pages} pages"

mon_livre = Livre("Le Rouge et le Noir", "Stendhal", 512)

print(mon_livre.get_titre())
mon_livre.set_titre("La Chartreuse de Parme")
print(mon_livre.get_titre())

print(mon_livre.get_nb_pages())
mon_livre.set_nb_pages(600)
print(mon_livre.get_nb_pages())
mon_livre.set_nb_pages("abc")
print(mon_livre.get_nb_pages())

print(mon_livre)
