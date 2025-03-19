# 11. Boucles `while`

## Introduction aux Boucles `while`

Les boucles `while` sont un élément fondamental en programmation Python, permettant d'exécuter un bloc de code tant qu'
une condition spécifique est remplie. Pour comprendre leur fonctionnement, il est utile de les comparer aux instructions
conditionnelles `if`.

### Comparaison avec `if`

Considérons deux exemples simples :

1. **Instruction `if`** :
   ```python
   x = 5
   if x < 10:
       print("x est inférieur à 10")
   ```

   Dans cet exemple, le message sera affiché une seule fois si `x` est inférieur à 10.

2. **Boucle `while`** :
   ```python
   x = 5
   while x < 10:
       print("x est inférieur à 10")
       x += 1
   ```

   Ici, le message sera affiché à chaque itération tant que `x` est inférieur à 10. La valeur de `x` est incrémentée à
   chaque itération pour éviter une boucle infinie.

### Différence Fondamentale

La différence clé entre `if` et `while` est la répétition :

- **`if`** vérifie une condition et exécute le code associé une seule fois si la condition est vraie.
- **`while`** continue d'exécuter le code tant que la condition est vraie.

### Nécessité de Mettre Fin à la Boucle

Pour éviter une **boucle infinie**, il est crucial de modifier la condition à l'intérieur de la boucle pour qu'elle
devienne fausse après un certain nombre d'itérations. Dans l'exemple ci-dessus, `x += 1` assure que la condition
`x < 10` deviendra fausse après plusieurs itérations.

Si la condition n'est jamais modifiée, comme dans l'exemple suivant, la boucle continuera indéfiniment :

```python
x = 5
while x < 10:
    print("x est inférieur à 10")
```

Cela entraînera une boucle infinie, car `x` reste toujours inférieur à 10.

En résumé, les boucles `while` sont puissantes pour répéter des actions, mais elles nécessitent une gestion soigneuse de
la condition pour éviter les boucles infinies.

## Validation des entrées

Voici un exemple de fonction Python qui utilise une boucle `while` pour demander à l'utilisateur d'entrer un nombre réel
supérieur à 0.

```python
def demander_nombre_positif():
    """
    Demande à l'utilisateur d'entrer un nombre réel supérieur à 0.
    
    Retourne le nombre une fois que la condition est satisfaite.
    """
    nombre = float(input("Veuillez entrer un nombre réel supérieur à 0 : "))

    # Boucle tant que le nombre n'est pas supérieur à 0
    while nombre <= 0:
        print("Le nombre doit être supérieur à 0.")
        nombre = float(input("Veuillez entrer un nombre réel supérieur à 0 : "))

    return nombre


# Exemple d'utilisation
nombre_positif = demander_nombre_positif()
print(f"Le nombre positif saisi est : {nombre_positif}")
```

Dans cette fonction, la boucle `while` continue de demander un nombre à l'utilisateur tant que celui-ci n'est pas
supérieur à 0. Une fois que la condition est satisfaite, la fonction retourne le nombre.

??? info "Exceptions (facultatif)"

      Si l'utilisateur n'entre pas un nombre valide (par exemple, une chaîne de caractères ou un symbole), la fonction
      précédente générera une erreur de type `ValueError`. Cela se produit car la fonction `float()` tente de convertir la
      saisie utilisateur en un nombre flottant, ce qui échoue si la saisie n'est pas un nombre.
      
      Pour résoudre ce problème, il est possible d'utiliser une gestion d'exceptions (`try-except`) pour capturer les
      erreurs de conversion et redemander à l'utilisateur de saisir un nombre valide. Voici une variation de la fonction
      précédente qui inclut cette gestion :
      
      ```python
      def demander_nombre_positif():
          """
          Demande à l'utilisateur d'entrer un nombre réel supérieur à 0.
          
          Retourne le nombre une fois que la condition est satisfaite.
          """
          nombre_valide = False
          nombre = None
          
          while not nombre_valide:
              try:
                  nombre = float(input("Veuillez entrer un nombre réel supérieur à 0 : "))
                  if nombre > 0:
                      nombre_valide = True
                  else:
                      print("Le nombre doit être supérieur à 0.")
              except ValueError:
                  print("La saisie n'est pas un nombre valide. Veuillez réessayer.")
          
          return nombre
      
      # Exemple d'utilisation
      nombre_positif = demander_nombre_positif()
      print(f"Le nombre positif saisi est : {nombre_positif}")

      ```
      
      Dans cette version, la boucle `while` continue indéfiniment jusqu'à ce que l'utilisateur entre un nombre réel supérieur
      à 0. Si la conversion en `float` échoue (ce qui déclenche une exception `ValueError`), un message d'erreur est affiché
      et l'utilisateur est invité à réessayer. Si le nombre est valide mais inférieur ou égal à 0, un message est également
      affiché pour demander un nombre supérieur à 0.

      Dans cette version, la variable `nombre_valide` agit comme _sentinelle_. La boucle continue tant que 
      `nombre_valide` est `False`. Dès que le nombre saisi est valide et supérieur à 0, `nombre_valide` est défini à 
      `True`, ce qui met fin à la boucle.

## Calcul de la Sommation $\sum_{i=1}^{n} \frac{1}{i}$

La sommation $\sum_{i=1}^{n} \frac{1}{i}$ est une série bien connue en mathématiques, souvent utilisée pour
illustrer les séries divergentes. Ici, nous allons écrire une fonction Python pour calculer cette sommation en utilisant
une boucle `while`.

### Fonction Python pour la Sommation

Voici une fonction Python qui calcule la sommation $\sum_{i=1}^{n} \frac{1}{i}$ en utilisant une boucle `while`.

```python
def sommation_inverse_while(n):
    """
    Calcule la sommation \sum_{i=1}^{n} 1/i en utilisant une boucle while.
    
    Arguments:
    n -- entier positif représentant la limite supérieure de la sommation.

    Retourne:
    La valeur de la sommation.
    """
    if n < 1:
        return 0

    somme = 0
    i = 1
    while i <= n:
        somme += 1 / i
        i += 1

    return somme


# Exemple d'utilisation
resultat = sommation_inverse_while(10)
print(f"La sommation est : {resultat}")
```

### Explications

1. **Définition de la Fonction** : La fonction `sommation_inverse_while(n)` prend un entier `n` comme argument et
   calcule la sommation des inverses de tous les entiers de 1 à `n`.
2. **Vérification de `n`** : La fonction vérifie si n est inférieur à 1. Si c'est le cas, elle retourne une valeur
   de 0. On pourrait lancer une erreur à la place avec `raise` (à voir plus tard).
3. **Calcul de la Sommation** : La sommation est calculée en utilisant une boucle `while` qui itère sur tous les entiers
   de 1 à `n` (inclus). À chaque itération, l'inverse de l'entier courant est ajouté à la somme.
4. **Retour de la Sommation** : Une fois que tous les termes ont été ajoutés, la fonction retourne la valeur de la
   sommation.
5. **Exemple d'Utilisation** : Dans l'exemple, nous calculons la sommation pour `n = 10`, ce qui donne une valeur
   approximative de `2.9289682539682538`.

!!! info "Info"

      Nous verrons dans le prochain chapitre une autre solution avec une boucle `for`.

## Calcul de la Racine Carrée avec une Boucle `while`

Le calcul de la racine carrée d'un nombre peut être abordé de plusieurs manières, notamment en utilisant des méthodes
numériques comme la méthode de Newton-Raphson ou une simple itération pour approximer la racine carrée. Ici, nous allons
utiliser une méthode simple basée sur l'itération pour trouver une approximation de la racine carrée d'un nombre.

### Problème

Le problème consiste à trouver un nombre `x` tel que `x * x` soit égal à un nombre donné `n`. Cependant, pour des
nombres non parfaits, il n'existe pas de solution exacte en termes de nombres rationnels. Nous devons donc nous
contenter d'une approximation.

### Fonction Python pour le Calcul de la Racine Carrée

Voici une fonction Python qui utilise une boucle `while` pour approximer la racine carrée d'un nombre en utilisant une
méthode simple d'itération.

```python
def racine_carree(n, precision=0.00001):
    """
    Approxime la racine carrée d'un nombre en utilisant une méthode d'itération.
    
    Arguments:
    n -- nombre pour lequel calculer la racine carrée.
    precision -- précision souhaitée pour l'approximation (par défaut : 0.00001).

    Retourne:
    L'approximation de la racine carrée.
    """
    if n < 0:
        raise ValueError("La racine carrée d'un nombre négatif n'est pas définie en nombres réels.")
    elif n == 0 or n == 1:
        return n  # Cas particuliers

    # Initialisation de la valeur de départ
    x = n / 2.0
    nouvelle_x = x + 1  # Pour garantir au moins une itération

    # Boucle d'itération
    while abs(x - nouvelle_x) >= precision:
        x = nouvelle_x
        nouvelle_x = (x + n / x) / 2.0

    return nouvelle_x


# Exemple d'utilisation
resultat = racine_carree(9)
print(f"La racine carrée de 9 est approximativement : {resultat}")
```

### Explications

1. **Définition de la Fonction** : La fonction `racine_carree(n, precision)` prend deux arguments : le nombre `n` pour
   lequel calculer la racine carrée et la précision souhaitée pour l'approximation.

2. **Vérification des Cas Particuliers** : Si `n` est négatif, la fonction lève une exception car la racine carrée d'un
   nombre négatif n'est pas définie en nombres réels. Si `n` est 0 ou 1, la fonction retourne directement `n`, car ce
   sont des cas simples.

3. **Initialisation des Valeurs** : La valeur initiale `x` est fixée à `n / 2.0`, ce qui est une estimation raisonnable
   pour commencer l'itération. Pour garantir au moins une itération, `nouvelle_x` est initialisée à `x + 1`.

4. **Boucle d'Itération** : La boucle `while` continue tant que la différence absolue entre `x` et `nouvelle_x` est
   supérieure ou égale à la précision souhaitée. Cela signifie que l'itération se poursuit jusqu'à ce que les
   approximations successives soient suffisamment proches.

5. **Calcul de la Nouvelle Approximation** : À chaque itération, la valeur de `x` est mise à jour avec la valeur
   précédente de `nouvelle_x`. Ensuite, une nouvelle approximation `nouvelle_x` est calculée en utilisant la formule
   `(x + n / x) / 2.0`, qui est une simplification de la méthode de Newton-Raphson pour la racine carrée.

6. **Retour de la Racine Carrée** : Une fois que la condition de précision est satisfaite, la fonction retourne la
   dernière valeur de `nouvelle_x`, qui est l'approximation finale de la racine carrée.

Cette méthode est efficace pour trouver une approximation précise de la racine carrée d'un nombre en utilisant une
boucle `while` avec une condition claire et concise.


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      