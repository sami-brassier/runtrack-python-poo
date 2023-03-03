def compare_strings(str1, str2):
    if str1 == str2:
        return 1
    if not str1 or not str2:
        return 0
    str2_parts = str2.split('*')
    start_pos = 0
    for part in str2_parts:
        pos = str1.find(part, start_pos)
        if pos == -1:
            return 0
        start_pos = pos + len(part)
    return 1

chaine1 = input("Entrez la première chaîne de caractères: ")
chaine2 = input("Entrez la deuxième chaîne de caractères: ")
resultat = compare_strings(chaine1, chaine2)
print(resultat)