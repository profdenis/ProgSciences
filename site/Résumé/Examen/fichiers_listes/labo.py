import matplotlib.pyplot as plt

nom_fichier = "labo3.csv"

with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()
    x = lignes[0].split(",")
    y = lignes[1].split(",")

for i in range(len(x)):
    x[i] = float(x[i])
for i in range(len(y)):
    y[i] = float(y[i])

fig = plt.figure(figsize=(5, 5))
plt.axis(False)
fig.set_facecolor("lightgrey")
plt.plot(x, y, ".r-", ms=10)

plt.show()