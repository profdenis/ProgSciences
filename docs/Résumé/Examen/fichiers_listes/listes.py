nombres = [1, 23, 3, -4, 5]
print(nombres)
print("longueur =", len(nombres))
print(nombres[1])

for x in nombres:
    print(x)

for i in range(len(nombres)):
    print(f"nombres[{i}] = {nombres[i]}")

r = list(range(5))
print(r)
