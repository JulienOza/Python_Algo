def verification_adn(saisie: str) -> bool:
    for char in saisie.lower():
        if char == "a" or char == "t" or char == "c" or char == "g":
            continue
        else :
            return False
    return True
    
        
saisie = (input("Saisir la séquence ADN : "))
print(verification_adn(saisie))