age = int(input("Entrez votre âge : "))
salaire = float(input("Entrez votre prétention salariale en euros : "))
experience = int(input("Entrez votre nombre d'années d'expérience : "))

if age < 30:
    print("Désolé, vous devez avoir au moins 30 ans pour postuler.")
if salaire > 40000:
    print("Désolé, le salaire demandé dépasse le maximum de 40 000 euros.")
if experience < 5:
    print("Désolé, vous devez avoir au moins 5 ans d'expérience.")

if age >= 30 and salaire <= 40000 and experience >= 5:
    print("Félicitations ! Votre candidature est valable pour ce poste.")
