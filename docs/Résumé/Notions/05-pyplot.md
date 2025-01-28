# 5. Module `pyplot`

## Introduction à `matplotlib.pyplot`

`matplotlib.pyplot` est un module de la bibliothèque **Matplotlib** qui fournit une interface simple et intuitive pour
créer des graphiques, inspirée de MATLAB. Chaque fonction de `pyplot` modifie une figure ou un graphique, permettant de
tracer, personnaliser et afficher des visualisations.


### 1. Création d'une figure : `plt.figure()`

La fonction **`plt.figure()`** crée une nouvelle figure ou active une figure existante. Une figure est le conteneur
principal pour un graphique.

**Exemple :**

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))  # Crée une figure de taille 8x6 pouces
```

- **Paramètres importants :**
    - `figsize=(width, height)`: Dimensions de la figure en pouces.
    - `dpi`: Résolution en points par pouce (par défaut 100).


### 2. Tracer des courbes : `plt.plot()`

La fonction **`plt.plot()`** trace des courbes reliant des points donnés par leurs abscisses et ordonnées.

**Exemple :**

```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, label="Courbe", color="blue", linestyle="--", marker="o")
plt.title("Exemple de graphique")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.legend()  # Ajoute une légende
```

- **Options courantes :**
    - `color`: Couleur de la courbe (`"red"`, `"blue"`, etc.).
    - `linestyle`: Style de ligne (`"--"`, `"-"`, etc.).
    - `marker`: Marqueur pour les points (`"o"`, `"s"`, etc.).


### 3. Afficher la figure : `plt.show()`

La fonction **`plt.show()`** affiche toutes les figures créées jusqu'à présent. Elle est indispensable pour visualiser
vos graphiques dans un script Python.

**Exemple :**

```python
plt.show()
```

- En mode interactif (comme Jupyter Notebook), cette commande est souvent implicite.


### 4. Histogrammes : `plt.hist()`

La fonction **`plt.hist()`** crée un histogramme pour visualiser la distribution des données.

**Exemple :**

```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, color="green", edgecolor="black")
plt.title("Histogramme")
```


### 5. Graphiques en barres : `plt.bar()`

La fonction **`plt.bar()`** trace des graphiques en barres verticales.

**Exemple :**

```python
categories = ["A", "B", "C"]
values = [10, 15, 7]

plt.bar(categories, values, color="purple")
plt.title("Graphique en barres")
```

### 6. Conversion entre figures multiples

Vous pouvez créer et gérer plusieurs figures avec **`figure()`** et basculer entre elles.

**Exemple :**

```python
f1 = plt.figure(1)
plt.plot([0, 1], [0, 1], label="Figure 1")
plt.legend()

f2 = plt.figure(2)
plt.plot([0, 1], [1, 0], label="Figure 2")
plt.legend()

plt.show()
```


### 7. Résumé des fonctions principales

| Fonction       | Description                             |
|----------------|-----------------------------------------|
| `plt.figure()` | Crée ou active une figure               |
| `plt.plot()`   | Trace une courbe                        |
| `plt.show()`   | Affiche toutes les figures              |
| `plt.hist()`   | Crée un histogramme                     |
| `plt.bar()`    | Trace un graphique en barres verticales |
| `plt.title()`  | Définit le titre du graphique           |
| `plt.xlabel()` | Définit l'étiquette de l'axe X          |
| `plt.ylabel()` | Définit l'étiquette de l'axe Y          |
| `plt.legend()` | Ajoute une légende au graphique         |


Avec ces outils de base de Matplotlib et son module Pyplot, vous pouvez créer rapidement des graphiques simples ou
complexes pour visualiser vos données efficacement !

??? note "Citations"

    - [1] https://docs.kanaries.net/fr/topics/Matplotlib/pyplot-figure
    - [2] https://www.geeksforgeeks.org/matplotlib-figure-figure-show-in-python/
    - [3] https://courspython.com/introduction-courbes.html
    - [4] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
    - [5] https://matplotlib.org/stable/api/pyplot_summary.html
    - [6] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    - [7] https://matplotlib.org/stable/tutorials/pyplot.html
    - [8] https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.show.html
    - [9] https://stackoverflow.com/questions/2397791/how-can-i-show-figures-separately

-------

!!! note "Note"
    Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
    **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
    structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.