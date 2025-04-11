# 18. Boucles imbriquées

Les boucles imbriquées sont un concept important en programmation, particulièrement utile pour traiter des données
multidimensionnelles ou répéter des actions de manière itérative selon plusieurs critères. Voici une introduction aux
boucles imbriquées en Python, illustrée par un exemple de table de multiplication.

## Introduction aux boucles imbriquées

Une boucle imbriquée est une boucle placée à l'intérieur d'une autre boucle. La boucle extérieure contrôle le nombre
d'itérations de la boucle intérieure. Chaque fois que la boucle extérieure effectue une itération, la boucle intérieure
s'exécute entièrement[1].

## Exemple : Table de multiplication

Voici un exemple simple de boucles imbriquées pour créer une table de multiplication de 1 à 10 :

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()  # Nouvelle ligne après chaque rangée
```

Dans cet exemple :

- La boucle extérieure (`for i in range(1, 11)`) contrôle les lignes de la table.
- La boucle intérieure (`for j in range(1, 11)`) gère les colonnes.
- `print(f"{i * j:4}", end="")` affiche le produit de `i` et `j`, formaté pour occuper 4 espaces.
- Le `print()` après la boucle intérieure crée une nouvelle ligne après chaque rangée[5].

Ce code produira une table de multiplication 10x10, où chaque cellule contient le produit des indices de sa ligne et de
sa colonne[6].

!!! note "Exercice"

    Définissez une fonction pour afficher une table de multiplication de taille $n\times n$. La fonction doit accepter
    un paramètre `n` qui doit être plus grand que 0. Sinon, rien ne doit être affiché.

Les boucles imbriquées sont très utiles pour traiter des structures de données à plusieurs dimensions ou pour effectuer
des opérations complexes nécessitant plusieurs niveaux d'itération[1][2].

??? note "Citations"

      - [1] https://v2.ttrinfo.be/articles/programmation/python/boucles/python-boucles-imbriquees/
      - [2] https://www.fil.univ-lille.fr/~L1S1Info/last/cours/064-for.html
      - [3] https://www-info.iutv.univ-paris13.fr/~santini/M1102_2017_2018/2017_2018_M1102_Intro_Algo/ch10_coursExercices.pdf
      - [4] https://r.qcbs.ca/workshop05/book-fr/boucles-for-dans-des-boucles-for..html
      - [5] https://www.elephorm.com/formation/code-data/c/apprendre-la-programmation-c/creer-une-table-de-multiplication-avec-une-boucle-en-c
      - [6] https://v2.ttrinfo.be/articles/programmation/python/boucles/python-boucles-imbriquees/python-boucles-imbriquees.pdf
      - [7] http://ressources.unit.eu/cours/Cfacile/co/Chap5_p8.html
      - [8] http://coursphysiquetsi.e-monsite.com/medias/files/cours-1.pdf
      - [9] https://abs.traduc.org/abs-5.3-fr/ch10s02.html
      - [10] https://cscircles.cemc.uwaterloo.ca/tag/boucles-imbriquees/
      - [11] https://www.youtube.com/watch?v=WBLbuJlF7kA
      - [12] https://portail.lyc-la-martiniere-diderot.ac-lyon.fr/srv1/co/boucle_for_1.html
      - [13] https://depinfo.u-cergy.fr/~tliu/ens/intro/correction-intro-info-4.pdf
      - [14] https://www.youtube.com/watch?v=ZMjF4JcR7Go
      - [15] https://www.collegerenecassincancale.ac-rennes.fr/spip.php?article177
      - [16] https://librecours.net/modules/dev/js10/solweb/co/imbrication.html
      - [17] https://codegym.cc/fr/groups/posts/fr.665.boucles-imbriquees-java
      - [18] https://education.vex.com/stemlabs/fr/cs/cs-level-1-vexcode-vr-python/moving-disks-with-loops/lesson-4-using-nested-loops
      - [19] https://codejumper.com/downloads/pdfs/lessons/fra/Code%20Jumper%20Lesson%2014%20Nested%20Loops_FRA.pdf
      - [20] https://www.ibisc.univ-evry.fr/~dupont/SUPPORTS/DupontCours/SiteProg/TD/Correction/td2_solution.pdf

## Exemple : somme de nombres entiers

Voici un exemple de programme utilisant des boucles while imbriquées pour répondre à votre demande :

```python
somme = 0
continuer = True

while continuer:
    entree_valide = False
    while not entree_valide:
        try:
            nombre = int(input("Entrez un nombre entier positif (ou 0 ou négatif pour terminer) : "))
            entree_valide = True
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    if nombre > 0:
        somme += nombre
    else:
        continuer = False

print(f"La somme des nombres entrés est : {somme}")
```

Ce programme fonctionne de la manière suivante :

1. La boucle extérieure (`while continuer:`) continue tant que l'utilisateur entre des nombres positifs.

2. La boucle intérieure (`while not entree_valide:`) s'assure que l'entrée est un entier valide :
    - Elle utilise un bloc try/except pour convertir l'entrée en entier.
    - Si la conversion réussit, `entree_valide` devient True et la boucle se termine.
    - Si une `ValueError` est levée (entrée non valide), un message d'erreur est affiché et la boucle continue.

3. Après la boucle intérieure, le programme vérifie si le nombre est positif :
    - Si oui, il est ajouté à la somme.
    - Sinon, `continuer` devient False, ce qui terminera la boucle extérieure.

4. Enfin, le programme affiche la somme totale des nombres positifs entrés.

Ce programme illustre bien l'utilisation de boucles while imbriquées pour gérer à la fois la validation des entrées (
boucle intérieure) et la logique principale du programme (boucle extérieure)[5][6].

??? note "Citations"

      - [1] https://www.datacamp.com/fr/tutorial/loops-python-tutorial
      - [2] https://python.jpvweb.com/python/mesrecettespython/doku.php?id=boucles_imbriquees
      - [3] https://librecours.net/modules/dev/js10/solweb/co/imbrication.html
      - [4] https://www.data-bird.co/blog/boucle-for-python
      - [5] https://www.ionos.fr/digitalguide/sites-internet/developpement-web/boucle-while-en-python/
      - [6] https://courspython.com/boucles.html
      - [7] https://www.reddit.com/r/learnpython/comments/1imx1me/python_nested_loop_for_and_while/?tl=fr
      - [8] https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/3-boucles/

## Exemple : somme de nombres entiers avec la fonction `lire_entier` :

```python
def lire_entier(invite="Entrez un nombre entier : "):
    entree_valide = False
    while not entree_valide:
        try:
            nombre = int(input(invite))
            entree_valide = True
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
    return nombre


def main():
    somme = 0
    continuer = True

    while continuer:
        nombre = lire_entier("Entrez un nombre entier positif (ou 0 ou négatif pour terminer) : ")

        if nombre > 0:
            somme += nombre
        else:
            continuer = False

    print(f"La somme des nombres entrés est : {somme}")


main()
```

## Fonction `lire_entier`

Cette fonction est conçue pour lire un entier saisi par l'utilisateur :

1. Elle prend un paramètre optionnel `invite` avec une valeur par défaut[6].
2. Elle utilise une boucle `while not entree_valide` pour continuer à demander une entrée jusqu'à ce qu'un entier valide
   soit fourni[5].
3. La fonction `input` est utilisée pour obtenir l'entrée de l'utilisateur sous forme de chaîne de caractères[9].
4. La conversion en entier est tentée avec `int()`[5].
5. Si la conversion réussit, l'entrée devient valide et on fait `entree_valide = True`.
6. En cas d'erreur (entrée non valide), un message d'erreur est affiché et la boucle continue.
7. Le nombre est retourné à la fin.

## Fonction `main`

Cette fonction contient la logique principale du programme :

1. Elle initialise une variable `somme` à 0 et une variable de contrôle `continuer` à `True`.
2. Une boucle `while` s'exécute tant que `continuer` est `True`.
3. À chaque itération, elle appelle `lire_entier` avec un message spécifique.
4. Si le nombre est positif, il est ajouté à la somme.
5. Si le nombre est 0 ou négatif, la boucle se termine en mettant `continuer` à `False`.
6. Après la boucle, la somme totale est affichée.

Cette structure permet de demander répétitivement des nombres à l'utilisateur, tout en gérant les erreurs de saisie et
en arrêtant le processus lorsqu'un nombre non positif est entré[1][2].

??? note "Citations"

     - [1] https://courspython.com/fonctions.html
     - [2] https://www.docstring.fr/glossaire/parametre/
     - [3] https://rtavenar.github.io/poly_python/content/chaines.html
     - [4] https://www.pierre-giraud.com/python-apprendre-programmer-cours/parametre-argument-fonction/
     - [5] https://www.pythoniaformation.com/blog/tutoriels-python-par-categories/projet-debutant-python-supercool/range-python
     - [6] https://docs.python.org/fr/dev/tutorial/controlflow.html
     - [7] https://python.sdv.u-paris.fr/07_fichiers/
     - [8] https://reeborg.ca/docs/fr/variables/arguments1b.html
     - [9] https://www.docstring.fr/formations/faq/ligne-de-commande/comment-lire-lentree-de-lutilisateur-en-python/
   

## Exemple : deviner un nombre

```python
import random

def lire_entier(invite="Entrez un nombre entier : "):
    entree_valide = False
    while not entree_valide:
        try:
            nombre = int(input(invite))
            entree_valide = True
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
    return nombre


def lire_entier_positif(invite="Entrez un nombre entier positif : "):
    entree_valide = False
    while not entree_valide:
        try:
            nombre = int(input(invite))
            if nombre > 0:
                entree_valide = True
            else:
                print("Ce nombre n'est pas plus grand que 0.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
    return nombre


def main():
    valeur_max = lire_entier_positif("Entrez la valeur maximale : ")
    invite = f"Devinez un nombre entier entre 1 et {valeur_max} inclusivement : "
    cible = random.randint(1, valeur_max)
    # print(cible)  # ne pas oublier d'effacer cette ligne
    essai = lire_entier(invite)
    while cible != essai:
        print("Incorrect ! Essayez de nouveau.")
        if essai < cible:
            print("Trop bas !")
        else:
            print("Trop haut!")
        essai = lire_entier(invite)

    print("Vous avez gagné !")

main()
```




-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.