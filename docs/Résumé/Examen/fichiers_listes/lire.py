nom_fichier = "nombres.txt"

print("Lecture du fichier")
with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()
    somme = 0
    for ligne in lignes:
        x = int(ligne)
        if x > 0:
            somme += x
    print("Le somme des nombres positifs est", somme)