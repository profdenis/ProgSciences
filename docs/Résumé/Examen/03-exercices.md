# Solutions

## Exercice 1 : Calcul et tracé de racines carrées

```python
import numpy as np
import matplotlib.pyplot as plt

# Lecture des nombres depuis le fichier
with open('valeurs.txt', 'r') as f:
    nombres = [int(ligne.strip()) for ligne in f.readlines()]

# Calcul des racines carrées
racines = np.sqrt(nombres)

# Tracé du graphique
plt.figure(figsize=(6, 4))
plt.plot(nombres, racines, 'bo-')
plt.title('Exercice 1 : Racines carrées')
plt.xlabel('Valeurs originales')
plt.ylabel('Racines carrées')
plt.grid(True)
plt.show()
```

## Exercice 2 : Températures et conversion

```python
import matplotlib.pyplot as plt

# Lecture des températures en Celsius
with open('temperatures.txt', 'r') as f:
    celsius = [float(ligne.strip()) for ligne in f.readlines()]

# Conversion en Fahrenheit
fahrenheit = [c * 9/5 + 32 for c in celsius]

# Tracé du graphique
plt.figure(figsize=(6, 4))
plt.plot(celsius, fahrenheit, 'r*-')
plt.title('Exercice 2 : Températures Celsius vs Fahrenheit')
plt.xlabel('Température (°C)')
plt.ylabel('Température (°F)')
plt.grid(True)
plt.show()
```

## Exercice 3 : Tracé d'une fonction trigonométrique

```python
import numpy as np
import matplotlib.pyplot as plt

# Lecture des angles en degrés
with open('angles.txt', 'r') as f:
    angles_deg = [float(ligne.strip()) for ligne in f.readlines()]

# Conversion en radians et calcul du sinus
angles_rad = np.radians(angles_deg)
sinus = np.sin(angles_rad)

# Tracé du graphique
plt.figure(figsize=(6, 4))
plt.plot(angles_deg, sinus, 'g^-')
plt.title('Exercice 3 : Sinus des angles')
plt.xlabel('Angle (degrés)')
plt.ylabel('Sinus')
plt.grid(True)
plt.show()
```

## Exercice 4 : Moyenne mobile

```python
import matplotlib.pyplot as plt

# Lecture des données
with open('donnees.txt', 'r') as f:
    donnees = [float(ligne.strip()) for ligne in f.readlines()]

# Calcul de la moyenne mobile sur 3 valeurs
moyennes_mobiles = []
for i in range(2, len(donnees)):
    moyenne = sum(donnees[i-2:i+1]) / 3
    moyennes_mobiles.append(moyenne)

# Tracé du graphique
plt.figure(figsize=(6, 4))
plt.plot(donnees, 'b-', label='Données originales')
plt.plot(range(2, len(donnees)), moyennes_mobiles, 'r-', label='Moyenne mobile (3)')
plt.title('Exercice 4 : Moyenne mobile sur 3 valeurs')
plt.xlabel('Index')
plt.ylabel('Valeur')
plt.legend()
plt.grid(True)
plt.show()
```

## Exercice 5 : Histogramme de valeurs

```python
import matplotlib.pyplot as plt

# Lecture des mesures
with open('mesures.txt', 'r') as f:
    mesures = [float(ligne.strip()) for ligne in f.readlines()]

# Création de l'histogramme
plt.figure(figsize=(6, 4))
plt.hist(mesures, bins=10, color='purple', edgecolor='black')
plt.title('Exercice 5 : Histogramme des mesures')
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.grid(True)
plt.show()
```

## Exercice 6 : Tracé de plusieurs jeux de données

```python
import matplotlib.pyplot as plt

# Lecture du fichier CSV
with open('experiment.csv', 'r') as f:
    lignes = f.readlines()

# Conversion des lignes en listes de floats
data = []
for ligne in lignes:
    valeurs = [float(x) for x in ligne.strip().split(',')]
    data.append(valeurs)

# Tracé des trois courbes
plt.figure(figsize=(6, 4))
couleurs = ['r', 'g', 'b']
for i, serie in enumerate(data):
    x = list(range(len(serie)))
    plt.plot(x, serie, marker='s', markersize=8, color=couleurs[i], label=f'Série {i+1}')

plt.title('Exercice 6 : Plusieurs jeux de données')
plt.xlabel('Index')
plt.ylabel('Valeur')
plt.legend()
plt.grid(True)
plt.show()
```
