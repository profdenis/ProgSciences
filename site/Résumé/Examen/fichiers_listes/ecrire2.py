nombres = [1, 23, 3, -4, 5, 65, 33, 23]
nom_fichier = "nombres2.txt"

print("Écriture du fichier")
# with open(nom_fichier, "w") as fichier:
#     n = len(nombres)
#     for i in range(n):
#         x = nombres[i]
#         fichier.write(f"{i},{x}\n")

with open(nom_fichier, "w") as fichier:
    for x in nombres:
        fichier.write(f"{x}\n")