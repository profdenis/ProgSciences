# 13. Boucle `for`

### Introduction aux Boucles `for`

Les boucles `for` sont un type de boucle en Python utilisées pour itérer sur des séquences, telles que des listes, des
tuples, des chaînes de caractères ou des plages de nombres générées par la fonction `range()`. Elles sont souvent
appelées "boucles comptées" car elles permettent d'exécuter un bloc de code un nombre fixe de fois, déterminé par la
longueur de la séquence sur laquelle elles itèrent.

### Boucles Comptées

Les boucles comptées sont utiles lorsque vous savez à l'avance combien de fois vous souhaitez exécuter un bloc de code.
Elles sont particulièrement pratiques pour parcourir des collections de données, comme des listes ou des tuples, où
chaque élément doit être traité individuellement.

### Comparaison avec les Boucles `while`

Les boucles `for` diffèrent des boucles `while` principalement par leur utilisation et leur syntaxe :

- **Boucles `while`** :
    - Utilisées lorsque le nombre d'itérations n'est pas connu à l'avance.
    - La condition d'arrêt est évaluée avant chaque itération.
    - Nécessitent une gestion explicite de la variable d'itération (par exemple, incrémenter une variable à chaque
      itération).

- **Boucles `for`** :
    - Utilisées lorsque le nombre d'itérations est connu ou déterminé par une séquence.
    - La variable d'itération est automatiquement définie et incrémentée à chaque itération.
    - Plus pratiques pour itérer sur des collections de données.

### Exemple de Boucle `for`

Voici un exemple simple de boucle `for` qui itère sur une liste de fruits et imprime chaque fruit :

```python
fruits = ["pomme", "poire", "abricot"]

for fruit in fruits:
    print(fruit)
```

Dans cet exemple, la boucle `for` itère sur la liste `fruits`, affectant à chaque itération la valeur de l'élément
courant à la variable `fruit`, puis imprime cette valeur.

### Utilisation de `range()`

Pour itérer sur une plage de nombres, vous pouvez utiliser la fonction `range()`, qui génère une séquence de nombres.
Voici un exemple :

```python
for i in range(5):
    print(i)
```

Cette boucle `for` itère sur les nombres de 0 à 4 (inclus), en imprimant chaque nombre à chaque itération.

### Avantages des Boucles `for`

Les boucles `for` sont généralement plus faciles à lire et à utiliser que les boucles `while` lorsque vous travaillez
avec des séquences ou des plages de nombres. Elles réduisent le risque d'erreurs liées à la gestion manuelle de la
variable d'itération et sont plus concises pour itérer sur des collections de données.

??? note "Citations"

    - [1] https://www.w3schools.com/python/python_for_loops.asp
    - [2] https://www.programiz.com/python-programming/for-loop
    - [3] https://www.scaler.com/topics/difference-between-for-and-while-loop-in-python/
    - [4] https://www.reddit.com/r/learnpython/comments/u88xcc/while_vs_for/
    - [5] https://www.scholarhat.com/tutorial/python/difference-between-for-and-while-loop-in-python
    - [6] https://www.simplilearn.com/tutorials/python-tutorial/python-for-loop
    - [7] https://www.reddit.com/r/learnpython/comments/1e3rnvz/whats_the_difference_between_a_while_loop_and_a/
    - [8] https://realpython.com/python-for-loop/
    - [9] https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python
    - [10] https://www.reddit.com/r/learnpython/comments/p47d1n/can_not_understand_for_loops/
    - [11] https://www.digitalocean.com/community/tutorials/python-for-loop-example
    - [12] https://www.coursera.org/tutorials/for-loop-python
    - [13] https://www.dataquest.io/blog/python-for-loop-tutorial/
    - [14] https://www.learnpython.org/en/Loops
    - [15] https://www.youtube.com/watch?v=dHANJ4l6fwA
    - [16] https://www.youtube.com/watch?v=I269TjuEVQA
    - [17] https://www.youtube.com/watch?v=WPF5M_Ic6Fc
    - [18] https://www.youtube.com/watch?v=3IMHXlyulO8
    - [19] https://www.youtube.com/watch?v=g1AFlLhgMR8
    - [20] https://wiki.python.org/moin/ForLoop
    - [21] https://www.youtube.com/watch?v=KWgYha0clzw
    - [22] https://www.simplilearn.com/tutorials/python-tutorial/python-loops
    - [23] https://www.ibm.com/reference/python/for-loop
    - [24] https://www.w3schools.com/python/python_while_loops.asp
    - [25] https://www.linode.com/docs/guides/python-for-and-while-loops/


## Calcul d'une sommation avec un `for`

Voici une version de [cette fonction](../11-while/#calcul-de-la-sommation-sum_i1n-frac1i) qui utilise une boucle 
`for` à la place de la boucle `while` pour calculer la sommation $\sum_{i=1}^{n} \frac{1}{i}$.

### Fonction avec Boucle `for`

```python
def sommation_inverse_for(n):
    """
    Calcule la sommation \sum_{i=1}^{n} 1/i en utilisant une boucle for.
    
    Arguments:
    n -- entier positif représentant la limite supérieure de la sommation.

    Retourne:
    La valeur de la sommation.
    """
    if n < 1:
        return 0

    somme = 0
    for i in range(1, n + 1):
        somme += 1 / i

    return somme


# Exemple d'utilisation
resultat = sommation_inverse_for(10)
print(f"La sommation est : {resultat}")
```

### Explications

1. **Définition de la Fonction** : La fonction `sommation_inverse_for(n)` prend un entier `n` comme argument et calcule
   la sommation des inverses de tous les entiers de 1 à `n`.

2. **Vérification de `n`** : Si `n` est inférieur à 1, la fonction retourne 0, car la sommation n'est pas définie pour
   `n < 1`.

3. **Boucle `for`** : La boucle `for` utilise la fonction `range(1, n + 1)` pour générer une séquence de nombres de 1 à
   `n` (inclus). À chaque itération, l'inverse de l'entier courant est ajouté à la somme.

4. **Retour de la Sommation** : Une fois que tous les termes ont été ajoutés, la fonction retourne la valeur de la
   sommation.

5. **Exemple d'Utilisation** : Dans l'exemple, nous calculons la sommation pour `n = 10`, ce qui donne une valeur
   approximative de 2.9289682539682538.

### Avantages de la Boucle `for`

Dans ce cas, la boucle `for` est plus concise et plus facile à lire que la boucle `while`, car elle évite la gestion
manuelle de la variable d'itération (`i`). La fonction `range()` génère automatiquement la séquence de nombres, ce qui
rend le code plus élégant et moins susceptible d'erreurs.




-------

??? info "Utilisation de l'IA"
        Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
        **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
        structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      