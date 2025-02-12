# Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant
# à l'utilisateur d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
# - choix n°1 : décider combien de notes il veut saisir, puis passer à la saisie de notes
# - choix n°2 : permissif, pourra saisir des notes en illimité jusqu'à entrer une note négative qui stoppera la saisie des notes.
# Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant d'avoir la note max,
#  la note min ainsi que la moyenne (possible de faire un menu pour choisir)
 
liste_notes= []

def saisie_limitee(nbre_notes):
    for i in range(nbre_notes):
        note = float(input(f"Saisir la note n°{i+1} : "))
        liste_notes.append(note)


def saisie_libre():
    note_stop = 0
    i = 0
    while note_stop >= 0:
        i += 1
        note = float(input(f"Saisir la note n°{i} : "))
        note_stop = note
        liste_notes.append(note)
    liste_notes.pop(-1)
        

# saisie_limitee(3)
saisie_libre()
print(liste_notes)