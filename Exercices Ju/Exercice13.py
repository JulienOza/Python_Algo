pop = float(input("Veuillez entrer la population initiale : "))
taux = float(input("Veuillez entrer le taux d'accroissement annuel : "))/100
pop_cible = float(input("Veuillez entrer la population cible : "))
annee = 0

if taux > 0 and pop_cible > pop :
    while pop < pop_cible:
        pop = pop * (1 + taux)
        annee += 1
        print(f"Année {annee}: Population = {pop:.2f}")
    print(f"La population cible a été atteinte après {annee} années.")

elif taux < 0 and pop_cible < pop : 
    while pop > pop_cible:
        pop = pop * (1 + taux)
        annee += 1
        print(f"Année {annee}: Population = {pop:.2f}")
    print(f"La population cible a été atteinte après {annee} années.")

else :
    print("Veuillez entrer des valeurs cohérentes")