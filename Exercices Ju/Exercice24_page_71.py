# Écrire un programme se servant d'une fonction retournant, à partir de deux nombres lui étant envoyés en paramètres :
# La somme
# La différence
# Le quotient
# Le produit
# Vous testerez cette fonction dans le cadre d'un programme console demandant à l'utilisateur deux valeurs et
# lui permettant d'obtenir les 4 résultats en même temps.

def op_numbers(a: int, b: int):

    somme = lambda a, b: round(a + b, 2)
    print(f"\nLa somme de '{a}' et '{b}' est {somme(a, b)} ")

    difference = lambda a, b: round(a - b, 2)
    print(f"\nLa difference de '{a}' et '{b}' est {difference(a, b)} ")

    quotient = lambda a, b: round(a / b, 2)
    print(f"\nLe quotient de '{a}' et '{b}' est {quotient(a, b)} ")

    produit = lambda a, b: round(a * b, 2)
    print(f"\nLe produit de '{a}' et '{b}' est {produit(a, b)} \n")

a = float(input("\nSaisir un nombre 'a' : "))
b = float(input("\nSaisir un nombre 'b' : "))

op_numbers(a, b)