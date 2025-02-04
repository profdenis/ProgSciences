# 1. Affichage sur la sortie standard

## La sortie standard

La sortie standard (`stdout`) est le flux de sortie par défaut d'un programme informatique[1][3]. C'est le canal par
lequel un programme affiche sa sortie normale à l'utilisateur ou à un autre programme[1].

Voici les principales caractéristiques de stdout :

1. Il s'agit d'un flux de données connecté par défaut au terminal ou à la console où le programme a été lancé[1][3].
2. Son descripteur de fichier est 1[3].
3. Il est utilisé pour afficher les résultats normaux, les messages d'information et les données produites par le
   programme[1][5].
4. En langage C, stdout est représenté par le pointeur FILE* stdout défini dans <stdio.h>[3].
5. Il peut être redirigé vers un fichier ou un autre programme, permettant ainsi de capturer ou de traiter la sortie du
   programme[3][5].
6. Par convention, stdout est utilisé pour la sortie normale, tandis que stderr (descripteur 2) est utilisé pour les
   messages d'erreur et de diagnostic[1][10].

La sortie standard permet aux programmes de communiquer leurs résultats de manière standardisée, facilitant ainsi leur
utilisation dans des scripts ou leur intégration avec d'autres outils[5].

??? note "Citations"

    - [1] [https://www.lenovo.com/fr/fr/glossary/stdout/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [https://www.ukonline.be/cours/java/apprendre-java/chapitre4-9](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://fr.wikipedia.org/wiki/Flux_standard](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] [https://fr.wikibooks.org/wiki/Programmation_C/Entr%C3%A9es/sorties](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [5] [https://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/scripts_and_streams/stdin_stdout_stderr.php](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://canada.lenovo.com/fr/ca/en/glossary/stdin/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://learn.microsoft.com/fr-fr/cpp/c-runtime-library/stdin-stdout-stderr?view=msvc-170](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [http://www.iro.umontreal.ca/~dift1166/A08/notesDeCours/intro_es.pdf](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [9] [https://librecours.net/modules/picasoft/init/linux-ligne-commande-api/solweb/co/flux.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [10] [https://www.reddit.com/r/bash/comments/w522np/understanding_stdin_stdout_and_stderr/?tl=fr](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)


-------

## La fonction `print()`

La fonction `print()` est utilisée pour afficher du texte ou des résultats à l'écran. Voici un guide détaillé pour
comprendre son fonctionnement avec plusieurs arguments, des séparateurs personnalisés et des fins de ligne différentes.

### 1. Imprimer plusieurs arguments

Vous pouvez passer plusieurs objets à `print()`, séparés par des virgules. Par défaut, Python insère un espace entre
eux.

```python
print("Bonjour", "tout", "le", "monde")
# Sortie : Bonjour tout le monde
```

### 2. Utiliser un séparateur personnalisé (`sep`)

Le paramètre `sep` permet de définir un séparateur spécifique entre les arguments.

```python
print("Bonjour", "tout", "le", "monde", sep="-")
# Sortie : Bonjour-tout-le-monde
```

### 3. Modifier la fin de ligne (`end`)

Par défaut, `print()` ajoute un saut de ligne (`\n`). Vous pouvez le changer avec le paramètre `end`.

```python
print("Bonjour", end=" ")
print("tout le monde")
# Sortie : Bonjour tout le monde (sur une seule ligne)
```

### **Exemple combiné**

Voici un exemple combinant les deux paramètres :

```python
print("Python", "est", "génial", sep="*", end="!\n")
# Sortie : Python*est*génial!
```

Ces fonctionnalités rendent la fonction `print()` très flexible pour formater vos sorties.

??? note "Citations"

    - [1] [https://www.ionos.fr/digitalguide/sites-internet/developpement-web/python-print/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [https://deeplearning.lipingyang.org/2017/03/11/print-multiple-arguments-in-python3/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://blog.alphorm.com/comprendre-et-manipuler-les-chaines-de-caracteres-en-python](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] [https://python.sdv.u-paris.fr/03_affichage/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [5] [https://www.geeksforgeeks.org/how-to-print-multiple-arguments-in-python/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://python.developpez.com/tutoriels/python-basic-par-exemple/?page=les-fonctions](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://www.w3schools.com/python/ref_func_print.asp](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [https://www.geeksforgeeks.org/how-to-pass-multiple-arguments-to-function/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [9] [https://www.geeksforgeeks.org/python-output-using-print-function/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)


-------

## Les *f-strings* en Python

Les **f-strings** (chaînes littérales formatées) sont une fonctionnalité introduite dans Python 3.6 pour simplifier le
formatage de chaînes. Elles permettent d'insérer des variables, des expressions ou des calculs directement dans une
chaîne de caractères, rendant le code plus lisible et concis.


### 1. Syntaxe de base

Pour créer une *f-string*, ajoutez la lettre **`f`** avant les guillemets de la chaîne. Utilisez des accolades `{}` pour
insérer des variables ou expressions.

```python
nom = "Alice"
age = 30
print(f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")
# Sortie : Bonjour, je m'appelle Alice et j'ai 30 ans.
```

### 2. Insérer des expressions

Les *f-strings* permettent d'évaluer des expressions directement dans les accolades.

```python
a = 5
b = 3
print(f"La somme de {a} et {b} est {a + b}.")
# Sortie : La somme de 5 et 3 est 8.
```


### 3. Formatage avancé

Vous pouvez appliquer un formatage précis à l'intérieur des accolades en utilisant des spécifications de format.

- **Nombres flottants** : Limiter le nombre de décimales.

```python
pi = 3.14159
print(f"La valeur de π est approximativement {pi:.2f}.")
# Sortie : La valeur de π est approximativement 3.14.
```

- **Alignement et largeur** :

```python
texte = "Python"
print(f"{texte:<10}")  # Aligné à gauche
print(f"{texte:>10}")  # Aligné à droite
print(f"{texte:^10}")  # Centré
```

### 4. Appels de fonctions

Les *f-strings* peuvent inclure des appels de fonctions ou des méthodes.

```python
nom = "alice"
print(f"Nom en majuscules : {nom.upper()}")
# Sortie : Nom en majuscules : ALICE
```

### 5. Exemple combiné

Voici un exemple combinant plusieurs fonctionnalités :

```python
nom = "Bob"
montant = 1234.56789
print(f"Bonjour {nom}, votre solde est de {montant:.2f} €.")
# Sortie : Bonjour Bob, votre solde est de 1234.57 €.
```

Les *f-strings* sont rapides, lisibles et flexibles, ce qui en fait un outil essentiel pour travailler avec des 
chaînes en Python.

??? note "Citations"

    - [1] [https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [2] [http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [3] [https://realpython.com/python-f-strings/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [4] https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
    - [5] [https://www.ionos.fr/digitalguide/sites-internet/developpement-web/python-f-strings/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [6] [https://www.docstring.fr/glossaire/f-string/](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [7] [https://he-arc.github.io/livre-python/fstrings/index.html](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)
    - [8] [https://www.w3schools.com/python/python_string_formatting.asp](https://www.erpi.com/fr/bundle-initiation-programmation-9782766157464.html)


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.