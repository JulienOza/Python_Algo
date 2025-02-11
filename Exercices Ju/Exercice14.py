print('Ce programme ecrit pour un intervalle souhaité "Fizz" pour les nombres entiers multipes de 3, "Buzz" pour les multiples de 5, "FizzBuzz" pour les multiple de 3 et 5')

for i in range (int(input("Veuillez saisir la limite basse de l'intervalle : ")),int(input("Veuillez saisir la limite haute de l'intervalle : "))) :
    if i%3 == 0 and i%5 == 0 :
        print("FizzBuzz")
    elif i%3 == 0 :
        print("Fizz")
    elif i%5 == 0 :
        print("Buzz")
    else : print(i)