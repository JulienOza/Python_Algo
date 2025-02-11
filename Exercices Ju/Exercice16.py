def soustraire (a: int, b: int):
    print(f'Je soustrais {b} de {a}')
    return (a - b)

a = int(input('Veuillez saisir un nombre "a" : '))
b = int(input('Veuillez saisir un nombre "b" : '))

resultat = soustraire(a, b)

print(f"Le résultat est {resultat}")