class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        nb_habitants = self.__ville.get_nb_habitants()
        nb_habitants += 1
        self.__ville._Ville__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville.get_nom()


ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

print(f"Population de la ville de {ville1.get_nom()}: {ville1.get_nb_habitants()} habitants")
print(f"Population de la ville de {ville2.get_nom()}: {ville2.get_nb_habitants()} habitants")

personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print(f"Mise a jour de la population de la ville de {ville1.get_nom()} {ville1.get_nb_habitants()} habitants")
print(f"Mise a jour de la population de la ville de {ville2.get_nom()} {ville2.get_nb_habitants()} habitants")