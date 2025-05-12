# 1. Exercices

## Questions

1. Calculer et afficher la valeur absolue d'un nombre entré par l'utilisateur.
2. Déterminer si le nombre _entier_ entré par l'utilisateur est pair ou impair.
3. Lire trois nombres et imprimer le plus petit de ces trois nombres.
4. Calculer le salaire total d'un employé. On lit en entrée les données concernant son salaire horaire et le nombre
   d'heures travaillées. Si l'employé a travaillé plus de 40 heures, les heures supplémentaires sont
   payées à 1.5 fois le salaire horaire.
5. Lire trois nombres positifs représentant la longueur des côtés d'un triangle. Imprimer :
    - "Scalène" si les trois côtés sont inégaux
    - "Isocèle" si deux des côtés sont égaux
    - "Équilatéral" si les trois côtés sont égaux
6. Un professeur vous fournit trois notes calculées sur 100. Calculer la moyenne et imprimer échec si la note finale est
   inférieure à 60/100. Dans le cas contraire, imprimer la note obtenue par l'étudiant.
7. Lire en entrée une note finale d'un cours. Si la note est plus petite que 0, ou si la note est plus grande que 100,
   alors afficher "Cette note est invalide" et terminer la fonction. Si la note est valide, alors vous devez afficher
   une lettre correspondant à la note selon les conditions suivantes :
    - **E** : plus petite que 60
    - **D** : de 60 à moins que 70
    - **C** : de 70 à moins que 80
    - **B** : de 80 à moins que 90
    - **A** : 90 ou plus
8. Vous devez lire un nombre entre 1 et 10 inclusivement.
    - Si le nombre n'est pas dans cet intervalle, alors afficher *"invalide"*.
    - Si le nombre est valide, alors afficher *"valide"*.
9. Vous devez lire un nombre entre 1 et 10 inclusivement.
    - Si le nombre n'est pas dans cet intervalle, alors afficher *"invalide"* et demander le nombre à nouveau. Vous
      devez vous assurer que le nombre est valide avant de continuer à la prochaine étape. Il n'y aucune limite sur
      le nombre d'essais incorrects.
    - Si le nombre est valide, alors afficher *"valide"*.
10. Vous devez lire un nombre entre 1 et 10 inclusivement.
    - Si le nombre n'est pas dans cet intervalle, alors afficher *"invalide"* et demander le nombre à nouveau. Vous
      devez vous assurer que le nombre est valide avant de continuer à la prochaine étape. Il y a une limite de 3 essais
      incorrects.
    - Si le nombre maximal d'essais incorrects a été atteint, alors afficher *"Nombre maximal d'essais atteint."* et la
      méthode doit se terminer.
    - Si le nombre est valide, alors afficher *"valide"*.
11. Vous devez lire un nombre _entier_ et l'afficher à l'envers. Par exemple, l'utilisateur saisit `123456` et le
    programme affiche `654321`. Pour cet exercice, vous ne pouvez pas inverser une chaîne de caractères qui représente
    le nombre, vous devez utiliser un `int` et utiliser la division et le modulo sur ce `int`.
12. Vous devez lire un nombre _entier_ et afficher un décompte à partir de ce nombre jusqu'à 0. Lorsque le décompte est
    terminé, afficher "Terminé !" à la place du nombre 0. Par exemple, si le nombre entré est 5, vous devez afficher
    ````
    5
    4
    3
    2
    1
    Terminé !
    ````