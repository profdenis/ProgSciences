noms = ["Denis", "Alice", "Bob", "John"]

noms[0] = "Jacques"
print(noms[0])
print(noms)

# noms[4] = "Jacqueline"
noms.append("Jacqueline")

print(noms[4])
print(noms)

print(noms[-1])
print(noms[len(noms)-1])
# print(noms[-10])

noms2 = noms[:-2]
print(noms2)

noms3 = noms[2:]
print(noms3)

noms4 = noms[1:3]
print(noms4)

copie = noms[:]
del noms[3]
print(noms)

copie.reverse()
print(copie)
copie.sort()
print(copie)

for nom in reversed(noms):
    print(nom)
for nom in sorted(noms):
    print(nom)
for nom in reversed(sorted(noms)):
    print(nom)