class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur

mon_rectangle = Rectangle(5, 3)

print(mon_rectangle.perimetre())
print(mon_rectangle.surface())

mon_rectangle.set_longueur(8)
print(mon_rectangle.get_longueur())

mon_parallelepipede = Parallelepipede(5, 3, 2)

print(mon_parallelepipede.perimetre())
print(mon_parallelepipede.surface())
print(mon_parallelepipede.volume())

mon_parallelepipede.set_hauteur(4)
print(mon_parallelepipede.get_hauteur())
