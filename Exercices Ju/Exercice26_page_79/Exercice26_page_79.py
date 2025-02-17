from modules import *

chaine_adn = saisie_adn(input("Veuillez saisir une chaîne ADN : "))
sequence_adn = saisie_adn(input("Veuillez saisir une séquence ADN à rechercher dans la chaîne : ").upper())

print(f"La séquence {sequence_adn} est présente dans {proportion(chaine_adn, sequence_adn)} % de la chaîne")