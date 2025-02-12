def verification_adn(saisie: str) -> bool:
    for char in saisie.lower():
        if char == "a" or char == "t" or char == "c" or char == "g":
            continue
        else :
            return False
    return True
    
        
# saisie = (input("Saisir la séquence ADN : "))
# print(verification_adn(saisie))

def saisie_adn(entree_sequence: str):
    if verification_adn(entree_sequence):
        return (entree_sequence)
    else :
        print("Erreur : veuillez entrer une séquence valide")

# entree_sequence = (input("Veuillez entrer une séquence ADN : "))
# print(saisie_adn(entree_sequence))

def proportion(chaine_adn: str, sequence_adn: str):
    return round((chaine_adn.count(sequence_adn)) * len(sequence_adn) / len(chaine_adn) * 100, 2)

chaine_adn = input("Veuillez saisir une chaîne ADN : ").lower()
sequence_adn = input("Veuillez saisir une sequence ADN à rechercher dans la chaîne : ").lower()

print(f"La séquence {sequence_adn} est présente dans {proportion(chaine_adn, sequence_adn)} % de la chaîne")

