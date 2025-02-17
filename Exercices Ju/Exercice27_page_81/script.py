import csv

product = [
    input("Entrez Titre : "),
    int(input("Entrer Prix : ")),
    int(input("Entrez Stock : "))
]


with open("Exercices Ju/Exercice27_page_81/stock.csv",mode='a',encoding="UTF-8",newline="") as fichier:
    writer = csv.writer(fichier,delimiter=";")
    writer.writerow(product)
   