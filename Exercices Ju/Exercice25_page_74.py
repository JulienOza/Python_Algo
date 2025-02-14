# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec :
# numéro de voie complément intitulé de voie commune
# code postal
# Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire.
# Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur.

annuaire = [
    {
        "numéro de voie": "12",
        "complément": "Bâtiment A",
        "intitulé de voie": "Rue de la Paix",
        "commune": "Paris",
        "code postal": 75002
    },
    {
        "numéro de voie": "45",
        "complément": "Appartement 3B",
        "intitulé de voie": "Avenue des Champs-Élysées",
        "commune": "Paris",
        "code postal": 75008
    },
    {
        "numéro de voie": "78",
        "complément": "",
        "intitulé de voie": "Boulevard Saint-Germain",
        "commune": "Paris",
        "code postal": 75006
    }
]

# Fonction d'affichage de toutes les adresses
def voir_adresses(ann):
    print("\n-- Tout l'annuaire --")
    i = 0
    for a in ann:
        i += 1
        print(f"""
*** Adresse {i} ***

Numéro de voie : {a['numéro de voie']}
Complément : {a['complément']}
Intitulé de voie : {a['intitulé de voie']}
Commune : {a['commune']}
Code postal : {a['code postal']}

---------------------------------------
""")
        
# voir_adresses(annuaire)

# Fonction d'affichage d'une adresse
def voir_adresse(ann, n):
    a=ann[n]

    print(f"""
Numéro de voie : {a['numéro de voie']}
Complément : {a['complément']}
Intitulé de voie : {a['intitulé de voie']}
Commune : {a['commune']}
Code postal : {a['code postal']}
""")
    
# voir_adresse(annuaire, 2)

# Fontion d'édition d'une adresse
def edit_adresse(ann, n):
    i = n-1
    a=ann[i]
    print(f"\n-- Modification de l'addresse {n} --" )
    a["numéro de voie"] = input("\nEntrez le nouveau numéro de voie : ")
    a["complément"] = input("Entrez le nouveau complément : ")
    a["intitulé de voie"] = input("Entrez le nouvel intitulé de voie : ")
    a["commune"] = input("Entrez la nouvelle commune : ")
    a["code postal"] = int(input("Entrez le nouveau code postal : "))

    print(f"""
*** Adresse {n} mise à jour ***
Numéro de voie : {a['numéro de voie']}
Complément : {a['complément']}
Intitulé de voie : {a['intitulé de voie']}
Commune : {a['commune']}
Code postal : {a['code postal']}
""")

# edit_adresse(annuaire, 2)


# Fonction de suppression d'une adresse
def supp_adresse(ann, n):
    ann.pop(n-1)
    print(f"\nL'addresse {n} a bien été supprimée")

# supp_adresse(annuaire, 1)
# voir_adresses(annuaire)


def ajout_adresse(ann):
    print("\n-- Ajout d'une nouvelle adresse --" )
    numero_de_voie = input("\nEntrez le numéro de voie: ")
    complement = input("\nEntrez le complément: ")
    intitule_de_voie = input("\nEntrez l'intitulé de voie: ")
    commune = input("\nEntrez la commune: ")
    code_postal = int(input("\nEntrez le code postal: "))

    nouv_adresse = {
        "numéro de voie": numero_de_voie,
        "complément": complement,
        "intitulé de voie": intitule_de_voie,
        "commune": commune,
        "code postal": code_postal
    }

    ann.append(nouv_adresse)

    print("\n*** Nouvelle adresse ajoutée *** ")
    voir_adresse(annuaire, -1)

# ajout_adresse(annuaire)

