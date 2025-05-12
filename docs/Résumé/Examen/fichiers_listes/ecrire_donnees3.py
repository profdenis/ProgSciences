import csv

ligne1 = [3, 6, 2, 8, 1]
ligne2 = [1, 7, -2, -12, 14]
ligne3 = [1, 2, 3, 4, 5]

lignes = [ligne1, ligne2, ligne3]

with open("donnees5.csv", "w", newline="") as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(lignes)


with open("donnees5.csv", "r") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)

