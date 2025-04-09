# 19. Fichiers

## Écrire dans un fichier

### Exemple

```python
import random

nom_fichier = "nombres.txt"

print("Écriture du fichier")
with open(nom_fichier, "w") as fichier:
    n = random.randint(1, 10)
    for i in range(n):
        x = random.randint(-100, 100)
        fichier.write(f"{x}\n")
```

Ce code génère un ensemble aléatoire de nombres entiers et les écrit dans un fichier texte. Voici une explication
détaillée:

## Analyse du code

1. `import random`: Cette ligne importe le module random qui permet de générer des nombres aléatoires en Python[5][9].

2. `nom_fichier = "nombres.txt"`: Définit le nom du fichier dans lequel les nombres seront écrits.

3. `print("Écriture du fichier")`: Affiche un message indiquant que le processus d'écriture du fichier commence.

4. `with open(nom_fichier, "w") as fichier:`: Ouvre le fichier en mode écriture ("w"). L'utilisation de l'instruction
   `with` garantit que le fichier sera correctement fermé après l'exécution du bloc d'instructions, même si une erreur
   se produit[1][7][10].

5. `n = random.randint(1, 10)`: Génère un nombre entier aléatoire entre 1 et 10 inclus. Ce nombre déterminera combien de
   nombres aléatoires seront générés et écrits dans le fichier[5][9][12].

6. `for i in range(n):`: Crée une boucle qui s'exécutera `n` fois.

7. `x = random.randint(-100, 100)`: À chaque itération de la boucle, génère un nombre entier aléatoire entre -100 et 100
   inclus[5][9].

8. `fichier.write(f"{x}\n")`: Écrit le nombre généré dans le fichier, suivi d'un retour à la ligne (`\n`). La notation
   `f"{x}"` est une f-string qui permet de formater facilement la chaîne de caractères avec la valeur de la variable
   `x`[1][4][10].

## Résultat

Après l'exécution de ce code, un fichier nommé "nombres.txt" sera créé dans le répertoire courant. Ce fichier contiendra
entre 1 et 10 nombres entiers aléatoires (compris entre -100 et 100), chacun sur une ligne distincte. Le nombre exact de
lignes est lui-même déterminé aléatoirement par la variable `n`.

Par exemple, si `n = 3`, le fichier pourrait contenir:

```
-42
78
-15
```

??? note "Citations"

     - [1] https://www.docstring.fr/formations/faq/fichiers/comment-lire-et-ecrire-dans-un-fichier-en-python/
     - [2] https://www.docstring.fr/formations/faq/librairie-standard/comment-generer-des-nombres-aleatoires-en-python/
     - [3] https://stackoverflow.com/questions/72163990/generate-random-numbers-and-write-to-text-file
     - [4] https://blog.alphorm.com/maitriser-la-manipulation-de-fichiers-en-python
     - [5] https://diveintopython.org/fr/learn/modules/popular-modules/random
     - [6] https://pynative.com/python-random-randrange/
     - [7] https://python.sdv.u-paris.fr/07_fichiers/
     - [8] https://docs.python.org/fr/3.13/library/random.html
     - [9] https://ioflood.com/blog/randint-python/
     - [10] https://python.doctor/page-lire-ecrire-creer-fichier-python
     - [11] https://openclassrooms.com/fr/courses/6204541-initiez-vous-a-python-pour-l'analyse-de-donnees/6252451-manipulez-des-nombres-aleatoires-avec-le-module-random
     - [12] https://www.w3schools.com/python/ref_random_randint.asp
     - [13] https://www.youtube.com/watch?v=qSYvF4GJWac
     - [14] https://www.workdispo.com/blog/random-python
     - [15] https://docs.python.org/3/library/random.html
     - [16] https://programminghistorian.org/fr/lecons/travailler-avec-des-fichiers-texte
     - [17] https://docs.python.org/fr/3.9/library/random.html
     - [18] https://www.cs2study.com/wp-content/uploads/2021/03/random-function.pdf
     - [19] https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/6-entrees-sorties/4-ecriture-fichier/
     - [20] https://www.ionos.fr/digitalguide/sites-internet/developpement-web/python-random/

## Lire le contenu d'un fichier

### Exemple

```python
import random

nom_fichier = "nombres.txt"

print("Lecture du fichier")
with open(nom_fichier, "r") as fichier:
    lignes = fichier.readlines()
    somme = 0
    for ligne in lignes:
        x = int(ligne)
        if x > 0:
            somme += x
    print("Le somme des nombres positifs est", somme)
```

Ce code lit un fichier texte contenant des nombres et calcule la somme des nombres positifs. Voici une explication
détaillée:

## Analyse du code

1. `import random`: Cette ligne importe le module random, bien qu'il ne soit pas utilisé dans le code présenté.

2. `nom_fichier = "nombres.txt"`: Définit le nom du fichier qui sera lu. Ce fichier doit contenir des nombres, chacun
   sur une ligne différente.

3. `print("Lecture du fichier")`: Affiche un message indiquant que le processus de lecture du fichier commence.

4. `with open(nom_fichier, "r") as fichier:`: Ouvre le fichier en mode lecture ("r"). L'utilisation de l'instruction
   `with` garantit que le fichier sera correctement fermé après l'exécution du bloc d'instructions[3][7].

5. `lignes = fichier.readlines()`: Lit toutes les lignes du fichier et les stocke dans une liste appelée `lignes`.
   Chaque élément de cette liste correspond à une ligne du fichier, y compris le caractère de fin de ligne (\n)[1][3].

6. `somme = 0`: Initialise une variable pour stocker la somme des nombres positifs.

7. `for ligne in lignes:`: Crée une boucle qui parcourt chaque ligne du fichier.

8. `x = int(ligne)`: Convertit la ligne (qui est une chaîne de caractères) en nombre entier.

9. `if x > 0:`: Vérifie si le nombre est positif (strictement supérieur à zéro).

10. `somme += x`: Si le nombre est positif, l'ajoute à la somme.

11. `print("Le somme des nombres positifs est", somme)`: Affiche le résultat final, c'est-à-dire la somme de tous les
    nombres positifs trouvés dans le fichier.

## Fonctionnement

Ce programme est conçu pour calculer la somme des nombres positifs contenus dans un fichier texte. Il ignore les nombres
négatifs et zéro. Par exemple, si le fichier "nombres.txt" contient:

```
12
23
-10
56
-45
```

Le programme calculera 12 + 23 + 56 = 91 et affichera "Le somme des nombres positifs est 91"[6][12].

Cette approche est couramment utilisée pour traiter des données numériques stockées dans des fichiers texte, en
appliquant des filtres (ici, seulement les nombres positifs) avant de réaliser des calculs[4][14].

??? note "Citations"

     - [1] https://blog.alphorm.com/maitriser-la-manipulation-de-fichiers-en-python
     - [2] https://www.mathweb.fr/euclide/2021/04/19/somme-des-chiffres-dun-nombre-en-python/
     - [3] https://www.docstring.fr/formations/faq/fichiers/comment-lire-et-ecrire-dans-un-fichier-en-python/
     - [4] https://profound.academy/fr/python-introduction/somme-des-chiffres-7pqPTN6mfw0DnYUYWTOF
     - [5] https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/6-entrees-sorties/2-lecture-fichier/
     - [6] https://openclassrooms.com/forum/sujet/exercice-python-moyenne
     - [7] https://numerique.ostralo.net/python_AideMemoire/09_Fichiers_texte.htm
     - [8] https://rtavenar.github.io/exos_python/gen/2_6_%20Nombres%20_%20somme%20des%20chiffres.html
     - [9] https://python.doctor/page-lire-ecrire-creer-fichier-python
     - [10] https://docs.python.org/fr/3.5/library/math.html
     - [11] https://www.zonensi.fr/Miscellanees/Bases_Python/Fichiers_Textes/
     - [12] https://www.reddit.com/r/learnpython/comments/pnvy6b/how_to_create_a_program_to_compute_the_sum_of/?tl=fr
     - [13] https://python.sdv.u-paris.fr/07_fichiers/
     - [14] https://profound.academy/fr/python-introduction/positifs-aenqxFhilm2M8wC7pt4S
     - [15] https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7300396-chargez-des-donnees-avec-python
     - [16] https://contester.asuscomm.com/fr/CourseTask_B.aspx?id=37953&idcourse=35158
     - [17] https://programminghistorian.org/fr/lecons/travailler-avec-des-fichiers-texte
     - [18] https://informathix.tuxfamily.org/?q=node%2F109
     - [19] https://clogique.fr/nsi/premiere/fichiers/fic1/
     - [20] https://www.data-bird.co/blog/guide-variables-python



-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
      