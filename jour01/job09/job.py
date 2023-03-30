class Student:
    def __init__(self, nom, prenom, id_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etudiant = id_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("id =", self.__id_etudiant)
        print("Niveau =", self.__level)
john_doe = Student("John", "Doe", 145)
john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)
print("Le nombre de crédits de", john_doe._Student__nom, john_doe._Student__prenom, "est de", john_doe._Student__credits, "points.")
john_doe.studentInfo()
