class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")

animal1 = Animal()
print(f"L'âge de l'animal est {animal1.age} ans")
animal1.vieillir()
print(f"L'âge de l'animal est {animal1.age} ans")
animal1.nommer("Luna")