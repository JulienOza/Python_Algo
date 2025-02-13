# Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant
# à l'utilisateur d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
# - choix n°1 : décider combien de notes il veut saisir, puis passer à la saisie de notes
# - choix n°2 : permissif, pourra saisir des notes en illimité jusqu'à entrer une note négative qui stoppera la saisie des notes.
# Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant d'avoir la note max,
#  la note min ainsi que la moyenne (possible de faire un menu pour choisir)
 
liste_notes= []

def saisie_limitee(nbre_notes):
    for i in range(nbre_notes):
        note = float(input(f"\nSaisir la note n°{i+1} : "))
        liste_notes.append(note)

def saisie_libre():
    note = 0
    i = 0
    while note >= 0:
        i += 1
        note = float(input(f"\nSaisir la note n°{i} : "))
        liste_notes.append(note)
    liste_notes.pop(-1)
    print("\nNote négative entrée, fin de la saisie")
    

while True:
    menu_depart = input("Veuillez choisir une methode de saisie :\n\n 1. Saisir un nombre de note choisi\n 2. Saisir un nombre de notes illimité, entrer une note negative pour stopper\n 3. Quitter\n\nRéponse : ")

    if menu_depart == "1":
        saisie_limitee(int(input("\nIndiquer le nombre de notes à saisir : ")))
        print(f"\nNotes saisies : {liste_notes}")
        break

    elif menu_depart == "2":
        saisie_libre()
        print(f"\nNotes saisies : {liste_notes}")
        break

    elif menu_depart == "3":
        print("\nAu revoir, à bientôt !")
        break

    else :
        print("\nErreur, saisissez une option valide")

while liste_notes != []:
    menu_notes = input("\nVeuillez choisir une option:\n\n 1. Note maximale\n 2. Note minimale\n 3. Moyenne des notes\n 4. Quitter\n\nRéponse : ")
    
    match menu_notes:
        case "1":
            print(f"\nNote maximale : {max(liste_notes)}")
        case "2":
            print(f"\nNote minimale : {min(liste_notes)}")
        case "3":
            print(f"\nNote Moyenne : {round(sum(liste_notes) / len(liste_notes), 2)}")
        case "4":
            print("\nAu revoir, à bientôt !")
            break
        case _:
            print("\nErreur, saisissez une option valide")
   