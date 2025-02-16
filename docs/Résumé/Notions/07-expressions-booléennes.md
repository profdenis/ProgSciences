# 7. Expressions booléennes

## Introduction au type `bool` en Python

Le type `bool` en Python est un type de données fondamental qui représente les valeurs booléennes. Il ne peut prendre
que deux valeurs possibles : `True` (vrai) ou `False` (faux)[1][2]. Ces valeurs sont utilisées pour effectuer des
opérations logiques et prendre des décisions dans les programmes.

Les booléens sont particulièrement utiles dans les structures conditionnelles et les boucles. Ils permettent d'évaluer
des conditions et de contrôler le flux d'exécution du programme.

## Expressions logiques

Les expressions logiques en Python utilisent des opérateurs de comparaison et des opérateurs logiques pour créer des
conditions complexes[2][4]. Voici les principaux opérateurs :

**Opérateurs de comparaison :**

- Égalité : `==`
- Inégalité : `!=`
- Supérieur à : `>`
- Inférieur à : `<`
- Supérieur ou égal à : `>=`
- Inférieur ou égal à : `<=`

**Opérateurs logiques :**

- ET logique : `and`
- OU logique : `or`
- NON logique : `not`

Ces opérateurs permettent de combiner des conditions simples pour former des expressions booléennes plus complexes.

## Tableau de priorité des opérateurs en Python

Voici un tableau indiquant la priorité des opérateurs en Python, des plus prioritaires aux moins prioritaires :

| Priorité | Opérateurs                                                          |
|----------|---------------------------------------------------------------------|
| 1        | Parenthèses `()`                                                    |
| 2        | Exposant `**`                                                       |
| 3        | Multiplication `*`, Division `/`, Division entière `//`, Modulo `%` |
| 4        | Addition `+`, Soustraction `-`                                      |
| 5        | Opérateurs de comparaison `<`, `<=`, `>`, `>=`, `==`, `!=`          |
| 6        | NON logique `not`                                                   |
| 7        | ET logique `and`                                                    |
| 8        | OU logique `or`                                                     |

Il est important de noter que les parenthèses ont la plus haute priorité et peuvent être utilisées pour forcer l'ordre
d'évaluation des expressions[2]. Les opérateurs logiques (`not`, `and`, `or`) ont la priorité la plus basse, ce qui
signifie qu'ils sont évalués en dernier dans une expression complexe[4].

En cas de doute sur l'ordre d'évaluation d'une expression, il est toujours recommandé d'utiliser des parenthèses pour
expliciter l'ordre souhaité et améliorer la lisibilité du code[2].

## Tables de vérité

### Table de vérité pour la négation (opérateur NOT)

L'opérateur `not` inverse la valeur de vérité de son opérande.

| `a`     | `not a` |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |


### Table de vérité pour la conjonction (opérateur AND)

L'opérateur `and` renvoie `True` uniquement si les deux opérandes sont `True`.

| `a`     | `b`     | `a and b` |
|---------|---------|-----------|
| `True`  | `True`  | `True`    |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |

### Table de vérité pour la disjonction (opérateur OR)

L'opérateur OR renvoie `True` si au moins l'un des opérandes est `True`.

| `a`     | `b`     | `a or b` |
|---------|---------|----------|
| `True`  | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |

Ces tables de vérité sont fondamentales pour comprendre le comportement des opérations logiques en programmation. Elles
sont particulièrement utiles lors de la construction de conditions complexes dans les structures de contrôle comme les
instructions if ou les boucles while.

??? note "Citations"

      - [1] https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/3-structures-conditionnelles/2-expressions-booleennes/
      - [2] https://cs.stanford.edu/people/nick/py/python-boolean.html
      - [3] https://www.docstring.fr/glossaire/boolean/
      - [4] https://www.linode.com/docs/guides/boolean-variables-in-python/
      - [5] https://www.ukonline.be/cours/python/apprendre-python/chapitre3-1
      - [6] http://perso.limsi.fr/pointal/python:booleens
      - [7] https://monlyceenumerique.fr/nsi_premiere/langages_de_prog_lp/lp2_structure_conditionnelle.php
      - [8] https://realpython.com/python-boolean/
      - [9] https://www.digitalocean.com/community/tutorials/understanding-boolean-logic-in-python-3
      - [10] https://codehs.com/tutorial/ryan/booleans-and-logical-operators-in-python
      - [11] https://realpython.com/python-and-operator/
      - [12] https://fr.wikibooks.org/wiki/Programmation_Python/Bool%C3%A9ens
      - [13] https://www.edlitera.com/blog/posts/python-booleans-comparison-operators-logical-operators
      - [14] https://koor.fr/Python/Tutorial/python_type_bool.wp
      - [15] https://www.docstring.fr/glossaire/and/
      - [16] https://egallic.fr/Enseignement/Python/operateurs.html
      - [17] https://docs.python.org/fr/3.6/reference/expressions.html
      - [18] https://python.developpez.com/tutoriels/apprendre-programmation-python/les-bases/?page=instruction-de-controle
      - [19] https://phys-mod.github.io/source/notebooks/python-intermediaire/02-logique-filtrage.html
      - [20] https://gayerie.dev/docs/python/python3/type_et_variable.html
      - [21] https://www.9raytifclick.com/cours/instructions-dentrees-sorties-print-input-en-python/
      - [22] https://fr.wikibooks.org/wiki/Programmation_Python/Op%C3%A9rateurs
      - [23] https://fr.wikibooks.org/wiki/Programmation_Python/Tableau_des_op%C3%A9rateurs
      - [24] https://www.ionos.fr/digitalguide/sites-internet/developpement-web/operateurs-python/
      - [25] https://www.pythonize.ir/fr/lecons/la_priorit%C3%A9/
      - [26] https://cahier-de-prepa.fr/pt-vauban/download?id=3584
      - [27] https://www.datacamp.com/fr/tutorial/python-operators-tutorial
      - [28] https://koor.fr/Python/Tutorial/python_operator_table_precedence.wp

-------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
    **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
    structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
              