def verification_adn(saisie: str) -> bool:
    for char in saisie.upper():
        if char not in "ACTG":
            return False
    return True

def saisie_adn(entree_sequence: str) -> str:
    while not verification_adn(entree_sequence):
        print("Erreur : veuillez entrer une séquence valide.")
        entree_sequence = input("Veuillez entrer une séquence ADN valide : ").upper()
    return entree_sequence

def proportion(chaine_adn: str, sequence_adn: str) -> float:
    return round((chaine_adn.count(sequence_adn)) * len(sequence_adn) / len(chaine_adn) * 100, 2)