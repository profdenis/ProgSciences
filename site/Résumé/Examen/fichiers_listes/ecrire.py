import random

nom_fichier = "nombres.txt"

print("Écriture du fichier")
with open(nom_fichier, "w") as fichier:
    n = random.randint(1, 10)
    for i in range(n):
        x = random.randint(-100, 100)
        fichier.write(f"{x}\n")
