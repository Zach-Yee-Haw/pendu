# Comment jouer au jeu du pendu :

## Objective:

L'objectif du jeu est de deviner toutes les lettres d'un mot en faisant moins de six erreurs.

## Mise en place:

1. Un mot est choisit au hasard à partir du fichier mots_pendu.txt.
2. Le joueur devine une lettre à la fois jusqu'à ce qu'il gagne, ou bien jusqu'à ce qu'il perde.

## Règles:

1. Lorsque la lettre fait partie du mot, toutes les instances de cette lettre sont révélées.
2. Si la lettre ne fait pas partie du mot, le joueur perd une vie et un morceau du pendu est dessiné.
3. S'il ne reste qu'une vie au joueur, il peut demander un indice. Celui-ci révèle au hasard une lettre parmis celles qui sont encore cachées.
4. La partie se termine quand:
   - Le mot est entièrement deviné.
   - Le joueur n'a plus de vies.
5. Le joueur peut décider de recommencer une partie lorsqu'elle se termine en tapant 'r' à la fin, suivit par la touche 'entrée'
