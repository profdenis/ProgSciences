import matplotlib.pyplot as plt
import numpy as np
nom_fichier = "nombres2.txt"

nombres = []

with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        x = int(ligne)
        nombres.append(x)

y = []
for i in nombres:
    y.append(i**2)

plt.figure(figsize=(5, 5))
plt.plot(nombres, y, ".r-")
plt.grid()
plt.show()