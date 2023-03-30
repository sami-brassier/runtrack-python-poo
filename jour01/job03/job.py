class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        print(f"Le nombre1 est {self.nombre1}")
        print(f"Le nombre2 est {self.nombre2}")

    def afficher_addition(self):
        resultat = self.nombre1+self.nombre2
        print(resultat)

operation1 = Operation(12,3)
operation1.afficher_addition()