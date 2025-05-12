nom_fichier = "nombres2.txt"

nombres = []

print("Lecture du fichier")
with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        x = int(ligne)
        nombres.append(x)

print(nombres)