class Personnage:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y -= 1
    
    def bas(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)

perso1 = Personnage(0, 0)

perso1.droite()

perso1.bas()

print(f"Le personnage est à la position {perso1.position()}")