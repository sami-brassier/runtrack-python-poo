class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age=age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)

professeur = Professeur(matiereEnseignee="Mathématiques", age=40)
professeur.bonjour()
professeur.enseigner()