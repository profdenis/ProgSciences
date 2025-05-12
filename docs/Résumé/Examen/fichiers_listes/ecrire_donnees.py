import csv

ligne1 = [3, 6, 2, 8, 1]
ligne2 = [1, 7, -2, -12, 14]
ligne3 = [1, 2, 3, 4, 5]

with open('donnees3.csv', 'w') as fichier:
    for x in ligne1[:-1]:
        fichier.write(f"{x},")
    fichier.write(f"{ligne1[-1]}\n")

    for x in ligne2[:-1]:
        fichier.write(f"{x},")
    fichier.write(f"{ligne2[-1]}\n")

    for x in ligne3[:-1]:
        fichier.write(f"{x},")
    fichier.write(f"{ligne3[-1]}\n")


with open("donnees3.csv", "r") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)

