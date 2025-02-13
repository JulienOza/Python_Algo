# Une année s'est écoulée et la nouvelle édition de la course de module de Tatooine est encore plus captivante. Cette année, la position de chaque concurrent est stockée dans une liste. (on y mettre le nom des concurrents) Parmi les moments phares de cette édition il y a :
# Une panne moteur fait passer le premier concurrent à la dernière position.
# Le second concurrent accélère et prend la tête de la course.
# Le dernier concurrent sauve l'honneur et dépasse l'avant-dernier module de la course.
# Un tir de blaster élimine le module en tête de la course.
# Dans un spectaculaire retournement de situation, un module qu'on pensait éliminé fait son grand retour à la dernière position.
# Créer la fonction panne_moteur, modifiant la liste passée en argument de manière à ce que le premier module passe dernier, le deuxième premier et ainsi de suite.
# Créer la fonction passe_en_tete, modifiant la liste passée en argument de manière à ce que le premier module passe deuxième et le deuxième premier.
# Créer la fonction sauve_honneur, modifiant la liste passée en argument de manière à ce que le dernier module passe avant dernier et l'avant dernier dernier.
# Créer la fonction tir_blaster, enlevant le premier concurrent de la liste passée en argument.
# Compléter la fonction retour_inattendu , ajoutant un concurrent à la fin de la liste passée en argument.

pos_racers =["racer1", "racer2", "racer3", "racer4", "racer5", "racer6" ]

def panne_moteur(liste):
    liste.append(liste[0])
    liste.pop(0)
    return liste

#print(panne_moteur(pos_racers))

def passe_en_tete(liste):
    liste[0], liste[1] = liste[1], liste[0]
    return liste

#print(passe_en_tete(pos_racers))

def sauve_honneur(liste):
    liste[-1], liste[-2] = liste[-2], liste[-1]
    return liste

#print(sauve_honneur(pos_racers))

def tir_blaster(liste):
    liste.pop(0)
    return liste

#print(tir_blaster(pos_racers))

def retour_inattendu(liste):
    liste.append("revenant")
    return liste

print(retour_inattendu(pos_racers))