# Écrire un algorithme permettant de saisir 15 notes et de les afficher.

ma_liste_2 = []
for i in range (15):
    note = int(input(f"Saisir la note {i + 1} : "))
    ma_liste_2.append(note)

print(ma_liste_2)