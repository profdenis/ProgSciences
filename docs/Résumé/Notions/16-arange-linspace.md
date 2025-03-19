# 16. Les fonctions `arange` et `linspace` de `numpy`

## La fonction `arange` de NumPy

La fonction `arange` de NumPy est utilisée pour créer un tableau de valeurs espacées régulièrement dans une plage
spécifiée. Elle est similaire à la fonction intégrée `range` de Python, mais elle retourne un tableau NumPy au lieu d'un
objet `range` ou d'une liste.

### Syntaxe et Paramètres

La syntaxe de `arange` est la suivante :

```python
numpy.arange([start, ] stop, [step, ] dtype = None)
```

- **start** : La valeur de départ de la plage. Si non spécifiée, elle est par défaut à 0.
- **stop** : La valeur de fin de la plage (exclue).
- **step** : L'incrément entre chaque valeur. Par défaut, il est à 1.
- **dtype** : Le type de données du tableau de sortie. Si non spécifié, il est déterminé automatiquement à partir des
  autres paramètres.

### Exemples d'utilisation

```python
import numpy as np

# Exemple 1 : Créer un tableau avec des valeurs de 0 à 9
arr1 = np.arange(10)
print(arr1)  # Output: [0 1 2 3 4 5 6 7 8 9]

# Exemple 2 : Créer un tableau avec des valeurs de 5 à 10 (exclusif)
arr2 = np.arange(5, 10)
print(arr2)  # Output: [5 6 7 8 9]

# Exemple 3 : Créer un tableau avec un pas personnalisé
arr3 = np.arange(5, 15, 2)
print(arr3)  # Output: [ 5  7  9 11 13]

# Exemple 4 : Créer un tableau avec des valeurs flottantes
arr4 = np.arange(1.5, 5.5, 0.5)
print(arr4)  # Output: [1.5 2.  2.5 3.  3.5 4.  4.5 5. ]
```

## Comparaison avec la fonction `range`

### Similitudes

- Les deux fonctions génèrent des séquences de nombres.
- Elles acceptent des paramètres similaires : `start`, `stop`, et `step`.

### Différences

- **Type de retour** : `range` retourne un objet `range` (un générateur en Python 3), tandis que `arange` retourne un
  tableau NumPy.
- **Support des flottants** : `range` ne prend en charge que les entiers, alors que `arange` peut gérer des valeurs
  flottantes.
- **Utilisation de la mémoire** : `range` est plus léger car il ne stocke pas toutes les valeurs en mémoire,
  contrairement à `arange` qui crée un tableau complet.
- **Performances** : Pour les grandes séquences, les opérations vectorisées de NumPy sont généralement plus rapides,
  mais si vous devez itérer explicitement, `range` peut être plus efficace en termes de mémoire et de vitesse[4].

### Choix entre `range` et `arange`

- Utilisez `range` pour des itérations simples sur des entiers ou pour des boucles où la mémoire est limitée.
- Utilisez `arange` lorsque vous avez besoin de travailler avec des tableaux NumPy, notamment pour des calculs
  vectorisés ou pour des valeurs flottantes.

??? note "Citations"

      - [1] https://sparkbyexamples.com/python/numpy-arange-function/
      - [2] https://www.reddit.com/r/learnpython/comments/3g0hiz/difference_between_range_and_arange/
      - [3] https://www.programiz.com/python-programming/numpy/methods/arange
      - [4] https://stackoverflow.com/questions/10698858/built-in-range-or-numpy-arange-which-is-more-efficient
      - [5] https://numpy.org/doc/2.1/reference/generated/numpy.arange.html
      - [6] https://pieriantraining.com/range-vs-arange-choosing-the-right-tool-for-your-python-code/
      - [7] https://realpython.com/how-to-use-numpy-arange/
      - [8] https://www.youtube.com/watch?v=Cs1oAnMZlWs
      - [9] https://www.w3resource.com/numpy/array-creation/arange.php
      - [10] https://www.youtube.com/watch?v=EgKkb1MXzTk
      - [11] https://ioflood.com/blog/numpy-np-arange/
      - [12] https://www.youtube.com/watch?v=Vx2iye1x7wg
      - [13] https://www.youtube.com/watch?v=uy2FF8KSj-E

## La fonction `linspace` de NumPy

La fonction `linspace` de NumPy est utilisée pour générer un tableau de nombres espacés régulièrement entre deux valeurs
spécifiées. Elle est particulièrement utile lorsque vous avez besoin d'un nombre précis de points entre deux valeurs, ce
qui est souvent le cas pour le tracé de courbes ou la simulation numérique.

### Syntaxe et Paramètres

La syntaxe de `linspace` est la suivante :

```python
numpy.linspace(start, stop, num, endpoint=True, retstep=False, dtype=None, axis=0)
```

- **start** : La valeur de départ de la plage.
- **stop** : La valeur de fin de la plage.
- **num** : Le nombre de valeurs à générer entre `start` et `stop`. Par défaut, il est à 50.
- **endpoint** : Un flag booléen indiquant si `stop` doit être inclus dans la séquence. Par défaut, il est à `True`.
- **retstep** : Un flag booléen indiquant si la fonction doit retourner le pas calculé entre les valeurs. Par défaut, il
  est à `False`.
- **dtype** : Le type de données du tableau de sortie. Si non spécifié, il est déterminé automatiquement à partir des
  autres paramètres.
- **axis** : Si `start` et `stop` sont des tableaux, cet argument spécifie sur quel axe les valeurs seront ajoutées. Par
  défaut, il est à 0.

### Exemples d'utilisation

```python
import numpy as np

# Exemple 1 : Créer un tableau avec 5 valeurs entre 0 et 1
arr1 = np.linspace(0, 1, 5)
print(arr1)  # Output: [0.  0.25 0.5  0.75 1.  ]

# Exemple 2 : Créer un tableau avec 5 valeurs entre 0 et 1, sans inclure la valeur de fin
arr2 = np.linspace(0, 1, 5, endpoint=False)
print(arr2)  # Output: [0.   0.2  0.4  0.6  0.8]

# Exemple 3 : Créer un tableau avec 5 valeurs entre 0 et 2π pour un tracé de courbe sinusoïdale
x = np.linspace(0, 2 * np.pi, 5)
y = np.sin(x)
print(x)  # Output: [0.         1.57079633 3.14159265 4.71238898 6.28318531]
print(y)  # Output: [ 0.         1.         0.        -1.         0.        ]
```

## Comparaison avec la fonction `arange`

### Similitudes

- Les deux fonctions génèrent des séquences de nombres.
- Elles acceptent des paramètres similaires pour le début et la fin de la séquence.

### Différences

- **Nombre de valeurs vs. pas** : `linspace` permet de spécifier le nombre de valeurs à générer (`num`), tandis que
  `arange` permet de spécifier le pas entre les valeurs (`step`).
- **Inclusion de la valeur de fin** : `linspace` inclut par défaut la valeur de fin (`endpoint=True`), alors que
  `arange` exclut la valeur de fin.
- **Précision pour les flottants** : `linspace` est plus précis pour les séquences de nombres flottants car il garantit
  que les valeurs de début et de fin sont incluses, ce qui réduit les erreurs de précision liées aux flottants.
- **Performances** : `arange` est généralement plus rapide car il utilise une progression arithmétique simple, tandis
  que `linspace` effectue des calculs supplémentaires pour garantir l'inclusion des valeurs de début et de fin.

### Choix entre `linspace` et `arange`

- Utilisez `linspace` lorsque vous avez besoin d'un nombre précis de points entre deux valeurs, comme pour le tracé de
  courbes ou la simulation numérique.
- Utilisez `arange` lorsque vous avez besoin d'un pas spécifique entre les valeurs, comme pour l'itération ou l'
  indexation.

??? note "Citations"

    - [1] https://fritz.ai/exploring-numpys-linspace-function/
    - [2] https://www.codecademy.com/resources/docs/numpy/built-in-functions/linspace
    - [3] https://www.statology.org/numpy-linspace-vs-arange/
    - [4] https://www.boardinfinity.com/blog/python-numpy-linspace/
    - [5] https://www.h2kinfosys.com/blog/create-a-range-of-numbers-as-an-array/
    - [6] https://www.programiz.com/python-programming/numpy/methods/linspace
    - [7] https://stackoverflow.com/questions/62106028/what-is-the-difference-between-np-linspace-and-np-arange
    - [8] https://realpython.com/np-linspace-numpy/
    - [9] https://note.nkmk.me/en/python-numpy-arange-linspace/
    - [10] https://www.thepythoncodingstack.com/p/difference-between-numpy-arange-and-linspace
    - [11] https://www.w3resource.com/numpy/array-creation/linspace.php
    - [12] https://docs.vultr.com/python/third-party/numpy/linspace
    - [13] https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html
    - [14] https://www.sharpsightlabs.com/blog/numpy-linspace/
    - [15] https://www.mathworks.com/help/matlab/ref/double.linspace.html
    - [16] https://www.youtube.com/watch?v=dRnUT5vVziU
    - [17] https://www.youtube.com/watch?v=9bHtS2tTLjI
    - [18] https://www.datacamp.com/tutorial/how-to-use-the-numpy-linspace-function
    - [19] https://ioflood.com/blog/np-linspace/
    - [20] https://python.plainenglish.io/title-numpy-linspace-vs-arange-which-to-choose-for-evenly-spaced-sequences-7ffb36ad98ca


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      

