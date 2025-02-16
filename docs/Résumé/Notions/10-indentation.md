# 10. Importance de l'indentation

## L'importance de l'indentation en Python

L'indentation est un aspect fondamental et distinctif de Python. Contrairement à de nombreux autres langages de
programmation qui utilisent des accolades ou des mots-clés pour délimiter les blocs de code, Python utilise
l'indentation. Cette approche rend le code plus lisible et force les programmeurs à structurer leur code de manière
cohérente.

### Rôle de l'indentation

1. **Délimitation des blocs :** L'indentation définit la structure et la hiérarchie du code en délimitant les blocs 
   d'instructions.

2. **Lisibilité :** Un code bien indenté est plus facile à lire et à comprendre, ce qui facilite la maintenance et la
   collaboration.

3. **Réduction des erreurs :** L'indentation obligatoire aide à prévenir certaines erreurs courantes liées à la
   structure du code.

### Fonctionnement de l'indentation

- **Début d'un bloc :** Un bloc de code commence après un deux-points `:` et est indenté par rapport à la ligne
  précédente.
- **Cohérence :** Toutes les lignes d'un même bloc doivent avoir la même indentation.
- **Fin d'un bloc :** Un bloc se termine lorsque l'indentation revient au niveau précédent ou à un niveau supérieur.

### Exemple d'indentation correcte

```python
def calculer_moyenne(notes):
    if len(notes) > 0:
        somme = 0
        for note in notes:
            somme += note
        moyenne = somme / len(notes)
        return moyenne
    else:
        return None


notes_eleve = [15, 12, 18, 10]
resultat = calculer_moyenne(notes_eleve)
if resultat is not None:
    print(f"La moyenne est : {resultat}")
else:
    print("Aucune note disponible")
```

Dans cet exemple, l'indentation montre clairement la structure du code :

- La fonction `calculer_moyenne` est définie au niveau principal.
- Le bloc `if-else` à l'intérieur de la fonction est indenté.
- La boucle `for` est encore plus indentée, montrant qu'elle est à l'intérieur du bloc `if`.

### Règles importantes

1. **Cohérence :** Utilisez toujours le même nombre d'espaces pour chaque niveau d'indentation. La norme PEP 8
   recommande 4 espaces.

2. **Pas de mélange :** Ne mélangez jamais les espaces et les tabulations pour l'indentation dans un même fichier.

3. **Alignement vertical :** Les lignes de continuation doivent s'aligner avec le délimiteur de parenthèse ouvrante ou
   utiliser un retrait suspendu.

### Erreurs courantes liées à l'indentation

1. **`IndentationError` :** Se produit lorsque l'indentation est incorrecte ou incohérente.

2. **`UnexpectedIndent` :** Apparaît quand une ligne est indentée alors qu'elle ne devrait pas l'être.

3. **`IndentationError: unexpected unindent` :** Se produit lorsqu'une ligne n'est pas suffisamment indentée par rapport
   au bloc précédent.

L'indentation en Python n'est pas seulement une convention stylistique, c'est une partie intégrante de la syntaxe du
langage. Une bonne compréhension et une application cohérente de l'indentation sont essentielles pour écrire du code
Python correct et lisible.



-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI, avec le *LLM*
      **Claude 3.5 Sonnet**. L'IA a été utilisée pour générer des explications, des exemples et/ou des suggestions de
      structure. Toutes les informations ont été vérifiées, éditées et complétées par l'auteur.
      