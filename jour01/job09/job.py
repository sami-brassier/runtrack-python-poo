class Produit:
    
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA/100)
    
    def afficher(self):
        print("Nom : ", self.nom)
        print("Prix HT : ", self.prixHT)
        print("TVA : ", self.TVA)
        print("Prix TTC : ", self.CalculerPrixTTC())
        
    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom
        
    def modifierPrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT
        
    def obtenirNom(self):
        return self.nom
    
    def obtenirPrixHT(self):
        return self.prixHT
    
    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Livre", 10, 5)
produit2 = Produit("Stylo", 1, 20)
produit3 = Produit("Ordinateur", 1000, 10)

produit1.afficher()
produit2.afficher()
produit3.afficher()

produit1.modifierNom("Cahier")
produit1.modifierPrixHT(5)
produit2.modifierNom("Crayon")
produit2.modifierPrixHT(0.5)
produit3.modifierNom("Tablette")
produit3.modifierPrixHT(800)

produit1.afficher()
produit2.afficher()
produit3.afficher()