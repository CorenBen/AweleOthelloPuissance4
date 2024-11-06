import sys
import random
sys.path.append("../..")
import game
import math

global ProfondeurMax
ProfondeurMax = 2

corner_tab = [[30, -10, 0, 0, 0, 0, -10, 30],
              [-10, -7, 0, 0, 0, 0, -7, -10],
              [ 0,   0, 0, 0, 0, 0,  0,  0 ],
              [ 0,   0, 0, 0, 0, 0,  0,  0 ],
              [ 0,   0, 0, 0, 0, 0,  0,  0 ],
              [ 0,   0, 0, 0, 0, 0,  0,  0 ],
              [-10, -7, 0, 0, 0, 0, -7, -10],
              [30, -10, 0, 0, 0, 0, -10, 30]]


stability_tab = [[4,  -3,  2,  2,  2,  2, -3,  4],
                 [-3, -4, -1, -1, -1, -1, -4, -3],
                 [2,  -1,  1,  0,  0,  1, -1,  2],
                 [2,  -1,  0,  1,  1,  0, -1,  2],
                 [2,  -1,  0,  1,  1,  0, -1,  2],
                 [2,  -1,  1,  0,  0,  1, -1,  2],
                 [-3, -4, -1, -1, -1, -1, -4, -3],
                 [4,  -3,  2,  2,  2,  2, -3,  4]]

INF = float("inf")

def scoreHeuristic(jeu):
    if(joueur == 1):
        scoreJoueur = jeu[4][0]
        scoreAdv = jeu[4][1]
    else:
        scoreJoueur = jeu[4][1]
        scoreAdv = jeu[4][0]

    return 100 * (scoreJoueur - scoreAdv) / (scoreAdv + scoreJoueur)


def stability_corner_Heuristic(jeu):
    stabilityJoueur = 0
    stabilityAdv = 0

    cornerJoueur = 0
    cornerAdv = 0

    for x in range(8):
        for y in range(8):
            if jeu[0][x][y] == joueur:
                stabilityJoueur += stability_tab[x][y]
                cornerJoueur += corner_tab[x][y]
            elif jeu[0][x][y] != 0:
                stabilityAdv += stability_tab[x][y]
                cornerAdv += corner_tab[x][y]

    if(stabilityJoueur == stabilityAdv):
        stability = 0
    else:
        stability = 100 * (stabilityJoueur - stabilityAdv) / (abs(stabilityJoueur) + abs(stabilityAdv))

    if(cornerJoueur == cornerAdv):
        corner = 0
    else:
        corner = 100 * (cornerJoueur - cornerAdv) / (abs(cornerJoueur) + abs(cornerAdv))

    return stability, corner


def evaluation(jeu):
    """ jeu -> float
        retourne le score d'evalution d'un etat de jeu
    """
    score = scoreHeuristic(jeu)
    stability, corner = stability_corner_Heuristic(jeu)

    return 5 * score + 10 * corner + 15 * stability


def minmax(jeu, coup, profondeur):
    """ jeu*coup*profondeur -> float
        Fonction récursive qui retourne un score d’utilité estimée
        pour un etat de jeu à partir d’appels de la fonction d’evaluation
        sur les feuilles de l’arbre (lorsque profondeur=pmax)
    """
    if(coup is None):
        copie = jeu
    else:
        copie = game.getCopieJeu(jeu)
        game.joueCoup(copie, coup)

    if(profondeur == ProfondeurMax):
        return evaluation(copie)

    if(game.finJeu(copie)):
        gagnant = game.getGagnant(copie)
        if(gagnant == joueur):
            return 100000000
        if(gagnant == 0):
            return -500
        return -100000000

    game.getCoupsValides(copie)

    if(len(copie[2]) == 0):
        copie[2] = None
        if(copie[1] == 1):
            copie[1] = 2
        else:
            copie[1] = 1
        return minmax(copie, None, profondeur)

    if(copie[1] == joueur):
        score = -INF
        for next in copie[2]:
            score = max(score, minmax(copie, next, profondeur+1))
    else:
        score = INF
        for next in copie[2]:
            score = min(score, minmax(copie, next, profondeur+1))

    return score


def decision(jeu, coups):
    """ jeu*List[coup] -> coup
        retourne le coup dont le score correspond au score d’évaluation maximal
        de la liste de coups passée en paramètre
    """
    scoreMax = -INF
    global joueur
    joueur = jeu[1]

    for coup in coups:
        score = minmax(jeu, coup, 1)
        if score > scoreMax:
            scoreMax = score
            coupMax = coup

    return coupMax

def saisieCoup(jeu):
    return decision(jeu, game.getCoupsValides(jeu))
