import sys
import random
sys.path.append("../..")
import game

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
params = []

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

    return params[0] * score + params[1] * corner + params[2] * stability

def estimation(jeu, coup):
    """ jeu*coup*profondeur -> float
        Fonction qui retourne un score d’utilité estimée pour un etat de jeu
    """
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    if(game.finJeu(copie)):
        gagnant = game.getGagnant(copie)
        if(gagnant == joueur):
            return 100000000
        if(gagnant == 0):
            return -500
        return -100000000
    return evaluation(copie)


def decision(jeu, coups):
    """ jeu*List[coup] -> coup
        retourne le coup dont le score correspond au score d’évaluation maximal
        de la liste de coups passée en paramètre
    """
    scoreMax = -INF
    global joueur
    joueur = jeu[1]

    for coup in coups:
        score = estimation(jeu, coup)
        if score > scoreMax:
            scoreMax = score
            coupMax = coup

    return coupMax

def getScoreCoup(jeu, coups):
    global joueur
    joueur = jeu[1]
    scores = [0 for i in coups]

    for i in range(len(coups)):
        scores[i] = estimation(jeu, coups[i])

    return scores

def saisieCoup(jeu):
    return decision(jeu, game.getCoupsValides(jeu))
