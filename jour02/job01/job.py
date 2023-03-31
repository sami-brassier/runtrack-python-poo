class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("Age :", self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age
    

class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")
    

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")
    

p = Personne()
e = Eleve()

e.affichageAge()
e.modifierAge(15)
e.affichageAge()

p.bonjour()

e.allerEnCours()

prof = Professeur("Informatique")
prof.enseigner()
