nbre_copie = float(input("Nombre de copies : "))

if nbre_copie > 20 :
    print(f"Remise niv.2 : le prix sera de {nbre_copie * 0.3}€")

elif nbre_copie >= 10 :
    print(f"Remise niv.1 : le prix sera de {nbre_copie * 0.4}€")

else :
    print(f"Le prix sera de {nbre_copie * 0.5}€")