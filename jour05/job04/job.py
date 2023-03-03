def plus_grand_chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        premier_chiffre = liste[0]
        reste_de_liste = liste[1:]
        plus_grand_reste = plus_grand_chiffre(reste_de_liste)
        if premier_chiffre > plus_grand_reste:
            return premier_chiffre
        else:
            return plus_grand_reste

liste = [1, 8, 5, 2, 7]
plus_grand_chiffre(liste)