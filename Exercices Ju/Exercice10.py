capital_init = float(input("Veuillez entrer le capital initial : "))
taux = float(input("Veuillez entrer le taux : "))/100
annee = 0
capital = capital_init

while capital < capital_init * 2:
    capital = capital * (1 + taux)
    annee += 1
    print(f"Année {annee}: Capital = {capital:.2f}")

print(f"Le capital a doublé après {annee} années.")