# 2. Lire des données sur l'entrée standard

## La fonction `input()` et la conversion en `int` ou `float`

La fonction `input()` permet de demander une saisie à l'utilisateur. Par défaut, elle retourne toujours une **chaîne de
caractères** (`str`). Si vous souhaitez utiliser cette entrée comme un nombre, il faut la convertir en un type numérique
comme `int` ou `float`.

### 1. Utilisation de base de `input()`

```python
nom = input("Quel est votre nom ? ")
print(f"Bonjour, {nom} !")
```

- **Explication** : Le texte entre parenthèses est affiché comme un message pour guider l'utilisateur.

### 2. Conversion en `int` ou `float`

Pour traiter des nombres, utilisez les fonctions de conversion `int()` ou `float()`.

```python
age = input("Quel âge avez-vous ? ")
age = int(age)  # Conversion en entier
print(f"Vous avez {age} ans.")
```

```python
poids = input("Quel est votre poids (en kg) ? ")
poids = float(poids)  # Conversion en nombre décimal
print(f"Votre poids est {poids} kg.")
```

### 3. Risque d'erreurs lors de la conversion

Si l'utilisateur saisit une valeur non convertible (par exemple, du texte au lieu d'un nombre), Python génère une erreur
de type **`ValueError`**.

**Exemple d'erreur :**

```python
valeur = input("Entrez un nombre : ")
valeur = int(valeur)  # Erreur si l'entrée n'est pas un nombre
# Si l'utilisateur tape "abc", l'erreur sera :
# ValueError: invalid literal for int() with base 10: 'abc'
```

### Points importants à retenir

- La conversion doit être utilisée uniquement si l'entrée est valide.
- Sans gestion d'erreurs (`try/except`), le programme s'arrêtera en cas de problème.

??? note "Citations"

    - [1] [https://www.w3schools.com/python/ref_func_input.asp](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [https://labex.io/questions/how-to-handle-type-conversion-errors-in-python-290726](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://www.docstring.fr/blog/interagir-avec-un-utilisateur-grace-la-fonction-in/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] [https://llego.dev/posts/handling-errors-exceptions-type-conversion-fails-python/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [5] [https://cscircles.cemc.uwaterloo.ca/5-fr/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://docs.python.org/fr/3/tutorial/errors.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://apprendre.modulo-info.ch/prog1/questionner.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [https://www.workdispo.com/blog/input-python](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)

-------

## Différences entre `int`, `round` et le formatage `.2f` dans les *f-strings*

### 1. Fonction `int`

- La fonction `int()` **tronque** toujours la partie décimale d'un nombre flottant, sans arrondi.
- Elle convertit un flottant en entier en supprimant tout ce qui suit la virgule.

**Exemple :**

```python
x = 5.76543
print(int(x))  # Sortie : 5
```

### 2. Fonction `round`

- La fonction `round()` **arrondit** un nombre au plus proche entier ou à un certain nombre de décimales.
- Par défaut, elle retourne un entier si aucun argument pour les décimales n'est fourni.
- Elle utilise l'arrondi "pair" (ou "round half to even") : si le chiffre après la virgule est exactement 0.5, il
  choisit l'entier **pair** le plus proche.

**Exemple :**

```python
x = 4.5
y = 5.5
print(round(x))  # Sortie : 4 (arrondi vers l'entier pair)
print(round(y))  # Sortie : 6 (arrondi vers l'entier pair)
```

Avec précision :

```python
z = 5.76543
print(round(z, 2))  # Sortie : 5.77 (arrondi à deux décimales)
```

!!! warning "Attention"

    Il est important de noter que `round` peut parfois donner des résultats surprenants en raison des limitations de la 
    représentation en virgule flottante. Par exemple :
    ```python
    print(round(2.675, 2))  # Résultat : 2.67 (au lieu de 2.68)
    ```


### 3. Formatage avec `.2f` dans les *f-strings*

- Le formatage `.2f` dans une f-string ne modifie pas la valeur réelle du nombre, mais contrôle uniquement son affichage
  en arrondissant visuellement à deux décimales.
- Contrairement à `round()`, il ne retourne pas un nouveau nombre, mais une chaîne formatée.

**Exemple :**

```python
x = 5.76543
print(f"{x:.2f}")  # Sortie : 5.77 (affichage arrondi à deux décimales)
```

### Différences entre `round` et `.2f`

| Fonctionnalité            | `round()`                 | `.2f` dans *f-strings*     |
|---------------------------|---------------------------|----------------------------|
| **Type de retour**        | Nombre (`int` ou `float`) | Chaîne de caractères       |
| **Modification réelle ?** | Oui                       | Non (affichage uniquement) |
| **Usage principal**       | Calculs                   | Formatage visuel           |

### Résumé des différences principales

- **`int()`** tronque sans arrondir.
- **`round()`** modifie réellement la valeur en arrondissant.
- **`.2f`** est utilisé pour afficher un nombre avec un format visuel précis sans changer sa valeur réelle.

??? note "Citations"

    - [1] [https://www.w3schools.com/python/ref_func_round.asp](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [https://geekflare.com/fr/round-numbers-in-python-with-examples/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://discuss.python.org/t/built-in-types-int-round-or-truncate-please-elaborate/24840](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] [https://waytolearnx.com/2020/07/fonction-round-python.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [5] [https://realpython.com/python-rounding/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://www.guru99.com/fr/round-function-python.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://www.geeksforgeeks.org/round-function-python/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [https://koor.fr/Python/API/python/builtins/round.wp](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [9] [https://stackoverflow.com/questions/43660910/python-difference-between-round-and-int](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)

-------

## Est-ce que les *f-strings* utilisent la règle "*round half to even*" comme la fonction round ?

Non, les ***f-strings*** en Python n'utilisent pas la règle "*round half to even*" comme la fonction `round()`.

Les *f-strings* avec un format comme `.2f` effectuent un **arrondi visuel** basé sur une règle d'arrondi classique
(*round half up*), où les valeurs à exactement 0.5 après le dernier chiffre significatif sont arrondies
**vers le haut**, indépendamment de la parité du chiffre précédent. En revanche, la fonction `round()` suit la règle
"*round half to even*" (ou "*banker's rounding*"), qui arrondit les valeurs à 0.5 vers l'entier pair le plus
proche[1][3][5].

**Exemple :**

```python
x = 2.5
print(f"{x:.0f}")  # Sortie : 3 (arrondi classique)
print(round(x))  # Sortie : 2 (arrondi pair)
```

??? note "Citations"

    - [1] [https://sparkbyexamples.com/python/python-limit-floats-to-two-decimal-points/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [https://rowannicholls.github.io/python/data/rounding_off.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://realpython.com/python-rounding/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] [https://en.wikipedia.org/wiki/Nearest_integer_function](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [5] [https://github.com/rust-lang/rust/issues/70336](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://gist.ly/youtube-summarizer/mastering-pythons-round-function-a-comprehensive-guide](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [https://schneide.blog/tag/python/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)



-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      