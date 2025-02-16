# 8. Conditionnelles

## Introduction aux conditionnelles en Python

Les structures conditionnelles sont essentielles en programmation car elles permettent à un programme de prendre des
décisions et d'exécuter différentes parties du code en fonction de certaines conditions. En Python, nous utilisons
principalement les instructions `if`, `else`, et `elif` pour créer ces structures conditionnelles.

## Instruction `if`

L'instruction `if` est la forme la plus simple de structure conditionnelle. Elle permet d'exécuter un bloc de code
uniquement si une condition donnée est vraie.

Syntaxe :

```python
if condition:
    # bloc de code à exécuter si la condition est vraie
```

Exemple :

```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```

Dans cet exemple, le message s'affichera uniquement si l'âge est supérieur ou égal à 18.

## Structure `if-else`

La structure `if-else` permet d'exécuter un bloc de code si la condition est vraie, et un autre bloc si elle est fausse.

Syntaxe :

```python
if condition:
    # bloc de code à exécuter si la condition est vraie
else:
    # bloc de code à exécuter si la condition est fausse
```

Exemple :

```python
age = 16
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

Dans ce cas, le programme affichera "Vous êtes mineur." car la condition `age >= 18` est fausse.

## Structure `if-elif-else`

La structure `if-elif-else` permet de tester plusieurs conditions successives. `elif` est une contraction de "else if".

Syntaxe :

```python
if condition1:
# bloc de code si condition1 est vraie
elif condition2:
# bloc de code si condition2 est vraie
elif condition3:
# bloc de code si condition3 est vraie
else:
# bloc de code si aucune des conditions précédentes n'est vraie
```

Exemple :

```python
note = 75

if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
elif note >= 60:
    print("Passable")
else:
    print("Insuffisant")
```

Dans cet exemple, le programme affichera "Bien" car la note est supérieure ou égale à 70 mais inférieure à 80.

**Points importants à retenir :**

1. L'indentation est cruciale en Python. Le bloc de code sous chaque condition doit être indenté.
2. Vous pouvez avoir autant de `elif` que nécessaire.
3. La partie `else` est optionnelle.
4. Seul le premier bloc dont la condition est vraie sera exécuté. Les autres blocs seront ignorés, même si leurs
   conditions sont également vraies.

En utilisant ces structures conditionnelles, vous pouvez créer des programmes qui prennent des décisions basées sur
différentes conditions, rendant votre code plus flexible et capable de gérer diverses situations.


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      