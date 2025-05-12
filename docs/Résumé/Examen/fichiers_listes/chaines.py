nom = "Denis"
liste = list(nom)

print(nom)
print(liste)

# nom[0] = "d"
liste[0] = "d"

print(liste)
nom = "".join(liste)
nom2 = " ".join(liste)
nom3 = "-".join(liste)
nom4 = " <--> ".join(liste)

print(nom)
print(nom2)
print(nom3)
print(nom4)

for lettre in nom:
    print(lettre)

print(len(nom))
print(nom.upper())
print(nom.lower())

print(nom[::2])
print(nom.count("i"))
print(nom.count("ni"))
print(nom.replace("s", "z"))

print(nom.split())
nom = "Denis Rinfret"
print(nom.split())
print(nom.split("i"))
