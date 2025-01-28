# 4. Module `numpy`

## Introduction à *NumPy* et ses fonctions mathématiques

**NumPy** est une bibliothèque essentielle pour le calcul scientifique en Python. Elle offre des outils puissants pour
effectuer des calculs mathématiques rapides et précis, notamment grâce à ses fonctions optimisées pour les tableaux 
(**ndarray**). Voici une introduction aux fonctions mathématiques de base de *NumPy*, incluant les logarithmes, racines
carrées, fonctions trigonométriques, et constantes mathématiques.

---

### 1. Constantes mathématiques : `np.e` et `np.pi`

*NumPy* fournit des constantes intégrées pour les nombres mathématiques importants :

- **`np.e`** : La base du logarithme naturel (environ 2.718).
- **`np.pi`** : La valeur de $$\pi$$ (environ 3.14159).

**Exemple :**

```python
import numpy as np

print(f"Constante e : {np.e}")
print(f"Constante pi : {np.pi}")
# Sortie :
# Constante e : 2.718281828459045
# Constante pi : 3.141592653589793
```


### 2. Logarithmes

*NumPy* propose plusieurs fonctions pour calculer différents types de logarithmes :

- **`np.log(x)`** : Logarithme naturel ($$\ln(x)$$).
- **`np.log10(x)`** : Logarithme décimal ($$\log_{10}(x)$$).

**Exemple :**

```python
x = np.array([1, np.e, 10])
print(np.log(x))  # Logarithme naturel
# Sortie : [0.         1.         2.30258509]

print(np.log10(x))  # Logarithme décimal
# Sortie : [0. 1. 1.]
```

### 3. Racine carrée

La fonction **`np.sqrt(x)`** calcule la racine carrée de chaque élément d'un tableau ou d'un nombre.

**Exemple :**

```python
x = np.array([4, 9, 16])
print(np.sqrt(x))
# Sortie : [2. 3. 4.]
```


### 4. Fonctions trigonométriques

*NumPy* propose des fonctions pour les calculs trigonométriques classiques :

- **`np.sin(x)`** : Calcule le sinus.
- **`np.cos(x)`** : Calcule le cosinus.
- **`np.tan(x)`** : Calcule la tangente.

Ces fonctions utilisent des angles exprimés en radians.

**Exemple avec radians :**

```python
angles = np.array([0, np.pi / 2, np.pi])
print(np.sin(angles))  # Sortie : [0. 1. 0.]
print(np.cos(angles))  # Sortie : [1. 0. -1.]
```

### 5. Conversion entre degrés et radians

Pour travailler avec des angles exprimés en degrés, *NumPy* propose deux fonctions utiles :

- **`np.radians(degrees)`** : Convertit des degrés en radians.
- **`np.degrees(radians)`** : Convertit des radians en degrés.

**Exemple :**

```python
deg = np.array([0, 90, 180])
rad = np.radians(deg)
print(rad)  # Sortie : [0.         1.57079633 3.14159265]

radians = np.array([0, np.pi / 2, np.pi])
deg = np.degrees(radians)
print(deg)  # Sortie : [  0.  90. 180.]
```


### Résumé des principales fonctions mathématiques de *NumPy*

| Fonction        | Description                           | Exemple d'utilisation                   |
|-----------------|---------------------------------------|-----------------------------------------|
| `np.e`          | Constante $$e$$                       | `np.e` → `2.718281828459045`            |
| `np.pi`         | Constante $$\pi$$                     | `np.pi` → `3.141592653589793`           |
| `np.log(x)`     | Logarithme naturel ($$\ln(x)$$)       | `np.log(10)` → `2.302585092994046`      |
| `np.log10(x)`   | Logarithme décimal ($$\log_{10}(x)$$) | `np.log10(100)` → `2.0`                 |
| `np.sqrt(x)`    | Racine carrée                         | `np.sqrt(16)` → `4.0`                   |
| `np.sin(x)`     | Sinus (angle en radians)              | `np.sin(np.pi/2)` → `1.0`               |
| `np.cos(x)`     | Cosinus (angle en radians)            | `np.cos(0)` → `1.0`                     |
| `np.tan(x)`     | Tangente (angle en radians)           | `np.tan(np.pi/4)` → `1.0`               |
| `np.radians(x)` | Conversion degrés → radians           | `np.radians(180)` → `3.141592653589793` |
| `np.degrees(x)` | Conversion radians → degrés           | `np.degrees(np.pi/2)` → `90.0`          |


Avec ces outils, *NumPy* simplifie considérablement les calculs scientifiques et numériques ! Vous pouvez maintenant
manipuler facilement des logarithmes, racines carrées et fonctions trigonométriques tout en travaillant avec des angles
exprimés en degrés ou radians.


-------

!!! note "Note"
     Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
     **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
     structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.