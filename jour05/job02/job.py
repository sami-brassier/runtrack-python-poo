def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x*x, n//2)
    else:
        return x * power(x, n-1)

x = int(input("Entrez un nombre x : "))
n = int(input("Entrez un nombre n : "))

resultat = power(x, n)

print(f"{x}^{n} = {resultat}")