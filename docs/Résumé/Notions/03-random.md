# 3. Importation de modules

## Exemple avec `random`

En Python, les **modules** sont des ensembles de fonctions et de variables prêtes à l'emploi. Pour utiliser un module,
il faut d'abord l'importer dans votre programme. Le module **`random`** est un exemple courant utilisé pour générer des
nombres aléatoires.

### 1. Importer le module `random`

Pour importer le module, utilisez la commande suivante :

```python
import random
```

Cela donne accès à toutes les fonctions du module `random`.

### 2. La fonction `randint`

La fonction **`randint(a, b)`** génère un entier aléatoire compris entre les bornes incluses $a$ et $b$.

**Syntaxe :**

```python
random.randint(a, b)
```

- **`a`** : borne inférieure (incluse).
- **`b`** : borne supérieure (incluse).

**Exemple :**

```python
import random

nombre = random.randint(1, 10)
print(f"Nombre entier aléatoire entre 1 et 10 : {nombre}")
```

- Si vous exécutez ce code plusieurs fois, il produira des entiers comme `3`, `7`, ou `10`.

### 3. La fonction `uniform`

La fonction **`uniform(a, b)`** génère un nombre flottant aléatoire compris entre $a$ et $b$, avec $a$ inclus
et $b$ potentiellement inclus.

**Syntaxe :**

```python
random.uniform(a, b)
```

- **`a`** : borne inférieure.
- **`b`** : borne supérieure.

**Exemple :**

```python
import random

nombre_flottant = random.uniform(1.5, 5.5)
print(f"Nombre flottant aléatoire entre 1.5 et 5.5 : {nombre_flottant}")
```

- Ce code peut produire des valeurs comme `2.34`, `4.78`, ou `5.5`.

### Résumé des différences entre `randint` et `uniform`

| Fonction        | Type de valeur générée | Bornes incluses ?                  |
|-----------------|------------------------|------------------------------------|
| `randint(a, b)` | Entier                 | Oui                                |
| `uniform(a, b)` | Flottant               | Oui pour $a$, $b$ potentiellement  |

Ces fonctions sont très utiles pour simuler des événements aléatoires ou générer des données de test dans vos programmes
Python.

??? note "Citations"

    - [1] https://www.cs.swarthmore.edu/~adanner/cs21/f09/randomlib.php
    - [2] https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
    - [3] https://www.geeksforgeeks.org/python-random-module/
    - [4] https://docs.python.org/zh-tw/3/library/random.html
    - [5] https://www.w3schools.com/python/ref_random_random.asp
    - [6] https://www.ionos.fr/digitalguide/sites-internet/developpement-web/python-randint/
    - [7] https://stackoverflow.com/questions/63246858/how-do-i-get-the-random-module-to-work-did-i-forget-to-import-something-or-d
    - [8] https://python-forum.io/thread-16247.html

## *Potentiellement incluse*

La borne supérieure $b$ est dite **"potentiellement incluse"** dans la fonction `random.uniform(a, b)` en raison des
limitations de l'arithmétique en virgule flottante utilisée par Python. Voici une explication détaillée :

1. **Comment fonctionne `random.uniform` :**
   La fonction génère un nombre aléatoire en utilisant la formule suivante :
   $a + (b - a) \times \text{random()}$,
   où `random()` produit un nombre flottant dans l'intervalle $[0, 1)$. En théorie, cela signifie que le résultat
   devrait être dans l'intervalle $[a, b)$, $b$ étant exclu.

2. **Effet des arrondis flottants :**
   En pratique, à cause des imprécisions liées au stockage des nombres en virgule flottante, il est possible que le
   calcul produise une valeur exactement égale à $b$. Cela dépend de la précision des calculs effectués par le
   processeur et de la représentation interne des nombres.

3. **Conséquences :**
    - Dans la plupart des cas, $b$ sera exclu.
    - Cependant, il est **rare mais possible** que $b$ soit inclus en raison d'arrondis spécifiques.

**Exemple :**

```python
import random

# Exemple où b pourrait être inclus
for _ in range(100000):
    x = random.uniform(0, 1)
    if x == 1:  # Vérifie si b est inclus
        print("La borne supérieure 1 a été incluse.")
        break
```

### Résumé

- La borne $b$ est **potentiellement incluse** dans `random.uniform(a, b)` à cause des arrondis flottants.
- Cela n'a généralement **aucune incidence pratique**, car les nombres générés sont continus et il y a une infinité de
  valeurs possibles entre $a$ et $b$.

??? note "Citations"

    - [1] https://www.w3schools.com/python/ref_random_uniform.asp
    - [2] https://stackoverflow.com/questions/78054851/when-using-random-uniforma-b-is-b-inclusive-or-exclusive
    - [3] https://numpy.org/doc/2.1/reference/random/generated/numpy.random.uniform.html
    - [4] https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/8-bibliotheque-standard/2-random/
    - [5] https://docs.python.org/fr/3.13/library/random.html
    - [6] https://scicomp.stackexchange.com/questions/29959/uniform-dots-distribution-in-a-sphere
    - [7] https://fiches-isn.readthedocs.io/fr/latest/random.html
    - [8] https://openclassrooms.com/fr/courses/6204541-initiez-vous-a-python-pour-lanalyse-de-donnees/6252451-manipulez-des-nombres-aleatoires-avec-le-module-random



-------

!!! note "Note"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.