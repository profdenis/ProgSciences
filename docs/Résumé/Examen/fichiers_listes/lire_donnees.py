import csv

with open('donnees2.csv', 'w') as fichier:
    for i in range(10):
        # fichier.write('ligne %d\n' % (i+1))
        # fichier.write(f"ligne {i+1}\n")
        fichier.write(f"{i},{i**2}\n")


with open("donnees2.csv", "r") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)

