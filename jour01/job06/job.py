class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
        
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur

rect = Rectangle(10, 5)

print("La Longueur est de ", rect.get_longueur())
print("La Largeur est de ", rect.get_largeur())

rect.set_longueur(15)
rect.set_largeur(7)

print("La Longueur est de ", rect.get_longueur())
print("La Largeur est de ", rect.get_largeur())
