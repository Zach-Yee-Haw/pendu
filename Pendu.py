import os
import random as rd
from unidecode import unidecode as udc

#On choisit un mot et on initialise les variables
choix_valides = 'abcdefghijklmnopqrstuvwxyz'
mots = open("mots_pendu.txt", "r", encoding='utf-8')
mots = mots.read()
mots = mots.split('\n')
while True:
    indice = False
    indice_utilise = False
    vies = 6
    lettres_devinees = []
    mot = []
    mot[:] = mots[rd.randrange(len(mots))-1]
    mot_ascii = udc(''.join(mot)).lower()
    mot_ascii_liste = []
    mot_ascii_liste[:] = mot_ascii.lower()
    mot_cache = ['_']*len(mot)
    i = 0

    #On révèle les charactères qui ne sont pas des lettres
    for lettre in mot_ascii_liste:
        if lettre not in choix_valides:
            mot_cache[i] = mot[i]
        i += 1
    while True:

        #On dessine l'état du jeu et on vérifie si le joueur a perdu
        if   vies == 6:
            print('___\n| |\n|\n|\n|\n|')
        elif vies == 5:
            print('___\n| |\n| O\n|\n|\n|')
        elif vies == 4:
            print('___\n| |\n| O\n| |\n|\n|')
        elif vies == 3:
            print('___\n| |\n| O\n|/|\n|\n|')
        elif vies == 2:
            print('___\n| |\n| O\n|/|\\\n|\n|')
        elif vies == 1:
            if indice_utilise == False: indice = True
            print('___\n| |\n| O\n|/|\\\n|/\n|')
        elif vies == 0:
            print('___\n| |\n| O\n|/|\\\n|/ \\\n|')
            print('Fin du jeu, vous avez perdu')
            print('Le mot était : ', ''.join(mot))
            break

        #On vérifie si le joueur a gagné
        if mot == mot_cache:
            print('Félicitation, vous avez gagné!')
            print('Mot trouvé : ', ''.join(mot_cache))
            break

        #On rappelle les lettres devinées et on demande une lettre au joueur
        print('Lettres devinées : ', ', '.join(lettres_devinees))
        print('Mot trouvé : ', ''.join(mot_cache))
        if indice == True:
            test = input('Entrez une lettre ou \'indice\' pour un indice : ').lower()
        else :
            test = input('Entrez une lettre : ').lower()
        os.system('cls') # Peut causer problèmes pour des ordinateurs utilisant MacOS ou Linux

        #Si le joueur veut un indice, on lui offre une lettre non-révélée
        if indice == True and test == 'indice':
            indice = False
            indice_utilise = True
            compte = 0
            lettres_restantes = []
            for i in range(len(mot_cache)):
                if mot_cache[i] == '_':
                    compte += 1
                    lettres_restantes.append(i)
            if compte > 1:
                position_a_reveler = rd.randrange(compte-1)
            else:
                position_a_reveler = 0
            position_lettre = lettres_restantes[position_a_reveler]
            test = mot_ascii_liste[position_lettre]

        # On vérifie si la lettre fait partie du mot et si elle est valide
        if udc(test) in lettres_devinees or len(test) != 1 or test not in choix_valides:
            print('Essai invalide!')
        elif test in mot_ascii_liste:
            print('Bien trouvé!')
            lettres_devinees.append(test)
            for i in range(len(mot)):
                if mot_ascii_liste[i-1] == test:
                    mot_cache[i-1] = mot[i-1]
        else:
            vies -= 1
            print('Dommage!')
            lettres_devinees.append(test)

        #On met les lettres devinées en ordre
        lettres_devinees.sort()

    #On vérifie si le joueur veut rejouer
    if input('\nTapez \'r\' pour recommencer, ou autre chose pour terminer\n') != 'r': break
    os.system('cls') # Peut causer problèmes pour des ordinateurs utilisant MacOS ou Linux
