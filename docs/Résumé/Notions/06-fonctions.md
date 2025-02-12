# 6. Définition de fonctions

## Introduction aux fonctions en programmation

Dans nos programmes précédents, nous avons déjà utilisé plusieurs fonctions sans les définir nous-mêmes.
Par exemple, nous avons employé `print()` pour afficher du texte à l'écran, `input()` pour demander une saisie à
l'utilisateur, et `numpy.cos()` (ou `np.cos()`) pour calculer le cosinus d'un angle. Ces fonctions sont des outils 
prédéfinis qui nous permettent d'effectuer des tâches spécifiques sans avoir à réécrire le code à chaque fois.

En programmation, les fonctions sont similaires aux fonctions mathématiques que vous connaissez déjà. Elles prennent des
entrées (appelées arguments ou paramètres), effectuent des opérations sur ces entrées, et produisent un résultat. Par
exemple, la fonction mathématique $f(x) = x^2$ prend un nombre $x$ en entrée et retourne son carré.

## Définition d'une fonction simple

Voyons maintenant comment définir notre propre fonction en Python. Prenons l'exemple d'une fonction qui calcule l'aire
d'un cercle.

```python
import numpy as np


def aire_cercle(rayon):
    aire = np.pi * rayon ** 2
    return aire
```

Examinons les différentes parties de cette définition de fonction :

1. **Signature de la fonction** : La ligne `def aire_cercle(rayon):` est la signature de la fonction. Elle commence par
   le mot-clé `def`, suivi du nom de la fonction et des paramètres entre parenthèses.

2. **Nom de la fonction** : `aire_cercle` est le nom que nous avons choisi pour notre fonction. Il est préférable de
   choisir un nom descriptif qui indique clairement ce que fait la fonction.

3. **Paramètre** : `rayon` est le paramètre de notre fonction. C'est la valeur d'entrée sur laquelle la fonction va
   travailler. Une fonction peut avoir plusieurs paramètres, séparés par des virgules.

4. **Corps de la fonction et indentation** : Le corps de la fonction contient les instructions qui seront exécutées
   lorsque la fonction sera appelée. En Python, le corps de la fonction est indenté (généralement de 4 espaces) pour
   indiquer qu'il fait partie de la fonction.

5. **Instruction _return_** : `return aire` spécifie la valeur que la fonction doit renvoyer lorsqu'elle est appelée. 
   Dans ce cas, elle renvoie l'aire calculée du cercle.

Pour utiliser cette fonction, nous pouvons maintenant l'appeler en lui fournissant un rayon :

```python
resultat = aire_cercle(5)
print(f"L'aire d'un cercle de rayon 5 est : {resultat}")
```

Cette approche nous permet de réutiliser facilement le code pour calculer l'aire de différents cercles sans avoir à
réécrire la formule à chaque fois.

## Définition d'une fonction avec plusieurs paramètres

En Python, il est très courant et souvent nécessaire de définir des fonctions qui prennent plusieurs paramètres. Cela
permet à une fonction d'être plus flexible et de traiter plusieurs entrées à la fois. Voici comment procéder :

### Syntaxe de base

La syntaxe pour définir une fonction avec plusieurs paramètres est similaire à celle d'une fonction avec un seul
paramètre, mais nous séparons les paramètres par des virgules dans la signature de la fonction.

```python
def nom_fonction(parametre1, parametre2, parametre3):
    # Corps de la fonction
    # Opérations utilisant les paramètres
    return resultat
```

### _Exemple_ : Calcul du volume d'une pyramide à 4 côtés

Pour calculer le volume d'une pyramide à 4 côtés (ou pyramide à base rectangulaire), nous avons besoin de trois 
paramètres : la longueur de la base, la largeur de la base, et la hauteur de la pyramide. La formule pour le volume 
est :

$V = \frac{1}{3} \times longueur \times largeur \times hauteur$.

Voici comment nous pouvons définir cette fonction en Python :

```python
def volume_pyramide(longueur, largeur, hauteur):
    volume = (1 / 3) * longueur * largeur * hauteur
    return volume
```

Dans cet exemple :

- `longueur`, `largeur`, et `hauteur` sont les trois paramètres de la fonction.
- La fonction utilise ces trois paramètres pour calculer le volume de la pyramide.
- Le résultat est renvoyé à l'aide de l'instruction `return`.

### Utilisation de la fonction

Pour utiliser cette fonction, nous fournissons les valeurs pour chaque paramètre dans l'ordre où ils sont définis :

```python
resultat = volume_pyramide(5, 5, 10)
print(f"Le volume d'une pyramide de base 5x5 et de hauteur 10 est : {resultat}")
```

### Points importants à retenir

1. **Ordre des paramètres** : L'ordre dans lequel vous définissez les paramètres est crucial. Lors de l'appel de la
   fonction, les arguments doivent être fournis dans le même ordre (longueur, largeur, hauteur).

2. **Nombre de paramètres** : Cette fonction a trois paramètres, ce qui est parfaitement acceptable. Cependant, si une
   fonction nécessite de nombreux paramètres, il peut être judicieux de considérer d'autres approches, comme
   l'utilisation d'un dictionnaire pour les regrouper.

3. **Noms des paramètres** : Notez comment les noms `longueur`, `largeur`, et `hauteur` sont descriptifs et clairs, ce
   qui rend la fonction plus facile à comprendre et à utiliser.

4. **Flexibilité** : Cette fonction peut calculer le volume de n'importe quelle pyramide à base rectangulaire, pas
   seulement celles à base carrée. Si la base est carrée, on peut simplement utiliser la même valeur pour la longueur et
   la largeur.

En utilisant des fonctions avec plusieurs paramètres comme celle-ci, vous pouvez créer des outils puissants et flexibles
pour résoudre une variété de problèmes en programmation.

## Erreurs courantes à éviter lors de la définition de fonctions en Python

### Erreurs de syntaxe

1. **Oublier les deux-points** : Toujours ajouter `:` à la fin de la ligne de définition de la fonction[3].

2. **Indentation incorrecte** : Le corps de la fonction doit être indenté, généralement de 4 espaces[3].

3. **Oublier les parenthèses** : Pour appeler une fonction, il faut utiliser des parenthèses, même si elle n'a pas 
   d'arguments[3].

### Erreurs de portée et de nommage

4. **Confusion entre variables locales et globales** : Les variables définies dans une fonction sont locales par défaut.
   
5. **Nommer une variable comme une fonction intégrée** : Éviter d'utiliser des noms comme `print` ou `input` qui
   masqueraient les fonctions Python intégrées[1].

### Erreurs liées aux arguments

6. **Inverser l'ordre des arguments** : Les arguments doivent être fournis dans le bon ordre. C'est pourquoi il est 
   important de bien nommer les paramètres.

7. **Trop de paramètres** : Limiter le nombre de paramètres pour maintenir la lisibilité et la simplicité de la
   fonction[9].

### Erreurs de conception

8. **Fonctions trop longues ou complexes** : Diviser les fonctions trop longues en sous-fonctions plus petites et plus
   simples[9].

9. **Retourner des types de données incohérents** : Une fonction devrait toujours retourner le même type de données,
   quelle que soit la branche d'exécution[14].

10. **Ne pas gérer les exceptions** : Utiliser des blocs `try/except` pour gérer les erreurs potentielles dans la
    fonction[15].

En évitant ces erreurs courantes, vous pourrez écrire des fonctions Python plus robustes et maintenables.

??? note "Citations"

     - [1] https://www.youtube.com/watch?v=IzNh3W2DY-w
     - [2] https://arjancodes.com/blog/python-common-pitfalls-and-fixes-for-syntactic-snafus/
     - [3] https://hackr.io/blog/common-python-mistakes
     - [4] https://rollbar.com/blog/python-errors-and-how-to-handle-them/
     - [5] https://docs.python-guide.org/writing/gotchas/
     - [6] https://doc.sagemath.org/html/en/tutorial/tour_functions.html
     - [7] https://www.reddit.com/r/learnpython/comments/pop076/error_the_function_is_not_defined/
     - [8] https://www.educative.io/blog/common-mistakes-python-programmers-how-to-fix
     - [9] https://www.kdnuggets.com/5-tips-for-writing-better-python-functions
     - [10] https://stackoverflow.com/questions/29690663/def-function-syntax-error-in-python-3/29690687
     - [11] https://stackoverflow.com/questions/1011431/common-pitfalls-in-python
     - [12] https://www.activestate.com/blog/top-10-coding-mistakes-in-python-how-to-avoid-them/
     - [13] https://docs.python.org/3/tutorial/errors.html
     - [14] https://betterstack.com/community/guides/scaling-python/python-errors/
     - [15] https://www.datacamp.com/tutorial/exception-handling-python
     - [16] https://stackoverflow.com/questions/19971453/is-it-bad-practice-in-python-to-define-a-function-in-the-middle-of-operational-c
     - [17] https://www.tutorialsteacher.com/python/error-types-in-python
     - [18] https://docs.python.org/ja/3.12/library/exceptions.html
     - [19] https://www.w3schools.com/python/python_functions.asp
     - [20] https://www.youtube.com/watch?v=zdJEYhA2AZQ


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      