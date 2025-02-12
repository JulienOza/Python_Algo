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

entree_sequence = (input("Veuillez entrer une séquence ADN : "))
print(saisie_adn(entree_sequence))