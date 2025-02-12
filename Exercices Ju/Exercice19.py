def verification_adn(saisie: str) -> bool:
    for char in saisie.lower():
        if char not in "atcg":
            return False
    return True

def saisie_adn(entree_sequence: str):
    while not verification_adn(entree_sequence):
        print("Erreur : veuillez entrer une séquence valide.")
        entree_sequence = input("Veuillez entrer une séquence ADN valide : ").lower()
    return entree_sequence

def proportion(chaine_adn: str, sequence_adn: str):
    return round((chaine_adn.count(sequence_adn)) * len(sequence_adn) / len(chaine_adn) * 100, 2)

chaine_adn = saisie_adn(input("Veuillez saisir une chaîne ADN : ").lower())
sequence_adn = saisie_adn(input("Veuillez saisir une séquence ADN à rechercher dans la chaîne : ").lower())

print(f"La séquence {sequence_adn} est présente dans {proportion(chaine_adn, sequence_adn)} % de la chaîne")

