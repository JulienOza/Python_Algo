n_max = int(input("Entrer le nombre n°1 : "))

for i in range (2,7) :
    n = int(input(f"Entrer le nombre n°{i} : "))
    if (n > n_max) :
        n_max = n

print(f"Le nombre le plus grand est {n_max}")