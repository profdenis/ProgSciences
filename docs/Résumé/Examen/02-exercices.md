# Exercices

## Exercice 1 : Calcul et tracé de racines carrées

Un fichier `valeurs.txt` contient une liste de nombres entiers (un nombre par ligne).  
Lis ces nombres, calcule leur racine carrée, puis trace le graphique des valeurs originales en fonction de leur racine
carrée.

**Étapes suggérées :**

1. Lire les nombres depuis le fichier.
2. Calculer la racine carrée de chaque nombre (utilise `np.sqrt`).
3. Tracer les points (nombres originaux, racines carrées) avec Matplotlib.

---

## Exercice 2 : Températures et conversion

Le fichier `temperatures.txt` contient des températures en Celsius (un nombre par ligne).  
Lis ces températures, convertis-les en Fahrenheit, puis trace la courbe des températures Celsius en fonction des
températures Fahrenheit.

**Formule de conversion :**  
$$ F = C \times \frac{9}{5} + 32 $$

---

## Exercice 3 : Tracé d'une fonction trigonométrique

Le fichier `angles.txt` contient des valeurs d’angles en degrés (un angle par ligne).  
Lis ces angles, calcule le sinus de chaque angle (pense à convertir en radians avec `np.radians`), puis trace la courbe
des angles (en degrés) en fonction de leur sinus.

---

## Exercice 4 : Moyenne mobile

Le fichier `donnees.txt` contient une série de nombres (un par ligne).  
Lis ces nombres et calcule la moyenne mobile sur 3 valeurs (chaque point est la moyenne de lui-même et des deux
précédents, à partir du 3e élément).  
Trace la série originale et la série des moyennes mobiles sur le même graphique (utilise deux courbes de couleurs
différentes).

---

## Exercice 5 : Tracé de plusieurs jeux de données

Un fichier `experiment.csv` contient 3 lignes avec des valeurs numériques séparées par des virgules.  
Écrire un programme qui :

1. Lit les 3 lignes
2. Convertit chaque ligne en liste de floats
3. Trace les trois courbes sur le même graphique avec des couleurs différentes (rouge, vert, bleu), en utilisant la
   position des nombres lus (les index dans les listes) comme valeur de x et les nombres lus comme valeurs de y.
4. Utilise des marqueurs carrés de taille 8 pour chaque point
