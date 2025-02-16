# 9. Correspondance de cas `match-case`

## Introduction au `match` en Python

Le `match` est une structure de contrôle introduite dans Python 3.10 qui permet d'effectuer une correspondance de motifs
structurelle. Cette fonctionnalité est similaire au `switch-case` d'autres langages de programmation, mais offre des
capacités plus avancées.

### Syntaxe de base

La syntaxe générale du `match` est la suivante :

```python
match expression:
    case motif1:
    # code à exécuter si motif1 correspond
    case motif2:
    # code à exécuter si motif2 correspond
    case _:
    # code à exécuter si aucun autre motif ne correspond
```

### Fonctionnement

1. L'expression après le mot-clé `match` est évaluée.
2. Cette valeur est comparée successivement à chaque motif défini par les clauses `case`.
3. Lorsqu'un motif correspond, le bloc de code associé est exécuté.
4. Si aucun motif ne correspond, le bloc de code associé au motif `_` (joker) est exécuté, s'il est présent.

### Exemples d'utilisation

**Correspondance simple :**

```python
def jour_type(jour):
    match jour:
        case "lundi" | "mardi" | "mercredi" | "jeudi" | "vendredi":
            return "jour ouvré"
        case "samedi" | "dimanche":
            return "week-end"
        case _:
            return "jour invalide"


print(jour_type("lundi"))  # Affiche : jour ouvré
print(jour_type("samedi"))  # Affiche : week-end
```

**Correspondance avec conditions :**

```python
def categoriser_nombre(x):
    match x:
        case x if x < 0:
            return "négatif"
        case 0:
            return "zéro"
        case x if x > 0:
            return "positif"


print(categoriser_nombre(-5))  # Affiche : négatif
print(categoriser_nombre(0))  # Affiche : zéro
print(categoriser_nombre(10))  # Affiche : positif
```

### Avantages du `match`

1. **Lisibilité :** Le code est souvent plus clair et plus concis qu'avec des `if-elif-else` multiples.
2. **Flexibilité :** Permet de correspondre à des structures de données complexes et d'extraire des valeurs.
3. **Performance :** Peut être plus efficace que des chaînes de `if-elif` pour de nombreux cas.

Le `match` est particulièrement utile pour traiter des structures de données complexes, implémenter des automates à
états finis, ou gérer différents types de messages dans des applications de traitement de données[1][2][5].

??? note "Citations"

      - [1] https://mimo.org/glossary/python/match-statement
      - [2] https://www.datamentor.io/python/match-case
      - [3] https://blog.stackademic.com/python-match-case-statement-63d01477e1c0
      - [4] https://www.tutorialspoint.com/python/python_matchcase_statement.htm
      - [5] https://www.youtube.com/watch?v=L7tT0NZF-Ag
      - [6] https://www.programiz.com/python-programming/match-case
      - [7] https://tonybaloney.github.io/posts/python-match-statement.html
      - [8] https://www.datacamp.com/tutorial/python-switch-case
      - [9] https://docs.python.org/3/whatsnew/3.10.html
      - [10] https://learnpython.com/blog/python-match-case-statement/
      - [11] https://guicommits.com/python-match-case-examples/
      - [12] https://peps.python.org/pep-0636/



-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      