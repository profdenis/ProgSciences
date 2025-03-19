# 14. La fonction `range`

La fonction `range()` est une fonction intégrée en Python qui génère une séquence de nombres entiers. Elle est
couramment utilisée dans les boucles `for` pour itérer sur une plage de valeurs. Cette fonction est très flexible grâce
à ses trois paramètres : `start`, `stop` et `step`.

---

### Syntaxe de `range()`

```python
range(start, stop, step)
```

- **`start`** (optionnel) : La valeur de départ de la séquence (incluse). Par défaut, elle est égale à 0.
- **`stop`** (obligatoire) : La valeur où la séquence s'arrête (non incluse).
- **`step`** (optionnel) : L'incrément entre chaque valeur de la séquence. Par défaut, il est égal à 1.

---

### Différents Cas d'Utilisation

#### 1. Un seul paramètre (`stop`)

Si un seul paramètre est fourni, il est interprété comme la valeur de `stop`. La séquence commence alors à 0 et
s'incrémente de 1 jusqu'à (mais sans inclure) `stop`.

```python
for i in range(5):
    print(i)
# Affiche : 0, 1, 2, 3, 4
```

---

#### 2. Deux paramètres (`start`, `stop`)

Avec deux paramètres, la séquence commence à `start` et s'arrête avant `stop`.

```python
for i in range(2, 6):
    print(i)
# Affiche : 2, 3, 4, 5
```

---

#### 3. Trois paramètres (`start`, `stop`, `step`)

Avec trois paramètres, la séquence commence à `start`, s'arrête avant `stop`, et utilise l'incrément spécifié par
`step`.

```python
for i in range(1, 10, 2):
    print(i)
# Affiche : 1, 3, 5, 7, 9
```

---

#### 4. Valeur négative pour `step`

Si le paramètre `step` est négatif, la séquence décroît. Dans ce cas, il faut que `start` soit plus grand que `stop`.

```python
for i in range(10, 0, -2):
    print(i)
# Affiche : 10, 8, 6, 4, 2
```

---

### Comparaison avec une Boucle `while`

Voici un exemple où nous utilisons une boucle `while` pour reproduire le comportement de `range()` :

**Avec une boucle `while` :**

```python
i = 1
while i < 10:
    print(i)
    i += 2
# Affiche : 1, 3, 5, 7, 9
```

**Avec une boucle `for` et `range()` :**

```python
for i in range(1, 10, 2):
    print(i)
# Affiche : 1, 3, 5, 7, 9
```

La boucle `for` avec `range()` est plus concise et réduit les erreurs liées à la gestion manuelle de l'incrémentation.

---

### Exemples Pratiques avec des Boucles `for`

#### Exemple 1 : Calculer une sommation simple

```python
somme = 0
for i in range(1, 6):  # Itère sur les nombres de 1 à (6-1)
    somme += i
print(f"La somme des nombres de 1 à 5 est {somme}")
# Affiche : La somme des nombres de 1 à 5 est 15
```

---

#### Exemple 2 : Itération avec un pas négatif

```python
for i in range(10, -1, -2):  # Compte à rebours par pas de -2
    print(i)
# Affiche : 10, 8, 6, 4, 2, 0
```

---

#### Exemple 3 : Table de multiplication

```python
n = int(input("Entrez un nombre pour voir sa table de multiplication : "))
for i in range(1, 11):  # Itère sur les nombres de 1 à (11-1)
    print(f"{n} x {i} = {n * i}")
```

---

### Points Clés

- La fonction `range()` génère des séquences efficaces en mémoire car elle ne crée pas réellement une liste mais génère
  les valeurs "à la volée".
- Les paramètres optionnels permettent un contrôle précis sur le début (`start`), la fin (`stop`) et l'incrément (
  `step`) de la séquence.
- Elle simplifie considérablement les boucles comptées par rapport aux boucles manuelles avec des variables d'itération.

En résumé, la fonction `range()` est un outil puissant et flexible pour contrôler les boucles en Python.

??? note "Citations"

    - [1] https://pynative.com/python-range-function/
    - [2] https://www.w3schools.com/python/gloss_python_for_range.asp
    - [3] https://www.w3schools.com/python/ref_func_range.asp
    - [4] https://sparkbyexamples.com/python/range-in-for-loop-in-python/
    - [5] https://realpython.com/python-range/
    - [6] https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/
    - [7] https://cs.stanford.edu/people/nick/py/python-range.html
    - [8] https://mimo.org/glossary/python/range-function
    - [9] https://stackoverflow.com/questions/71625642/python-range-and-for-loop-understanding
    - [10] https://www.snakify.org/lessons/for_loop_range/
    - [11] https://www.datacamp.com/tutorial/python-range-function
    - [12] https://www.datacamp.com/tutorial/python-for-i-in-range
    - [13] https://www.coursera.org/tutorials/python-range
    - [14] https://www.freecodecamp.org/news/python-range-function-example/


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      