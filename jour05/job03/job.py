def longueur(chaine):
    if chaine == '':
        return 0
    else:
        return 1 + longueur(chaine[1:])

chaine = "Hello, world!"
longueur_chaine = longueur(chaine)
print("La longueur de la chaîne", chaine, "est", longueur_chaine)