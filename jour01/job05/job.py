class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"La coordonnée x du point est {self.x}")
    
    def afficherY(self):
        print(f"La coordonnée y du point est {self.y}")
    
    def changerX(self, nouvelle_x):
        self.x = nouvelle_x
    
    def changerY(self, nouvelle_y):
        self.y = nouvelle_y

point1 = Point(3, 4)

point1.afficherLesPoints()

point1.afficherX()

point1.afficherY()

point1.changerX(5)

point1.changerY(6)

point1.afficherLesPoints()