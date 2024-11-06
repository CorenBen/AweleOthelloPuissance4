#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

ProfondeurMax = 4
INF = float("inf")


def scoreHeuristic(jeu):
    if(joueur == 1):
        adv = 2
        scoreJoueur = scoreAvant[0] - jeu[4][0]
        scoreAdv = scoreAvant[1] - jeu[4][1]
    else:
        adv = 1
        scoreJoueur = scoreAvant[1] - jeu[4][1]
        scoreAdv = scoreAvant[0] - jeu[4][0]

    if (scoreAdv + scoreJoueur != 0):
        return 100 * (scoreJoueur - scoreAdv) / (scoreAdv + scoreJoueur)
    return 0

def mobilityHeuristic(jeu):
    if(joueur == 1):
        adv = 2
    else:
        adv = 1

    tmp = game.getCoupsValides(jeu)
    if jeu[1] == joueur:
        coupJoueur = len(jeu[2])
        jeu[1], jeu[2] = adv, None
        game.getCoupsValides(jeu)
        coupAdv = len(jeu[2])
        jeu[1], jeu[2] = joueur, tmp
    else:
        coupAdv = len(jeu[2])
        jeu[1], jeu[2] = joueur, None
        game.getCoupsValides(jeu)
        coupJoueur = len(jeu[2])
        jeu[1], jeu[2] = adv, tmp

    return 100 * (coupJoueur - coupAdv) / (coupAdv + coupJoueur)


def stabilityHeuristic(jeu):
    stabilityJoueur = 0
    stabilityAdv = 0

    for i in range(5):
        if(jeu[0][joueur-1][i] == 1):
            stabilityAdv += val_tab[joueur-1][i]
        if(jeu[0][joueur-1][i] == 2):
            stabilityAdv += 4*val_tab[joueur-1][i]
        if(jeu[0][abs(joueur-2)][i] == 1):
            stabilityJoueur += val_tab[abs(joueur-2)][i]
        if(jeu[0][abs(joueur-2)][i] == 1):
            stabilityJoueur += 4*val_tab[abs(joueur-2)][i]

    if(stabilityAdv + stabilityJoueur != 0):
        return 100 * (stabilityJoueur - stabilityAdv) / (stabilityAdv + stabilityJoueur)

    return 0

def evaluation(jeu):
    """ jeu -> float
        Retourne le score d'evalution d'un etat de jeu
    """
    score = scoreHeuristic(jeu)

    mobility = mobilityHeuristic(jeu)

    stability = stabilityHeuristic(jeu)

    return  20 * score + 50 * mobility + 2 * stability


def alpha_beta(jeu, coup, alpha, beta, profondeur):
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    coupValides = game.getCoupsValides(copie)

    if(game.finJeu(copie)):
        gagnant = game.getGagnant(copie)
        if(gagnant == joueur):
            return 100000000
        if(gagnant == 0):
            return -500
        return -100000000

    if(profondeur == ProfondeurMax):
        return evaluation(copie)

    if(copie[1] == joueur):
        score = -INF
        for next in copie[2]:
            score = max(score, alpha_beta(copie, next, alpha, beta, profondeur+1))
            if(score >= beta):
                return score
            alpha = max(alpha, score)

    else:
        score = INF
        for next in copie[2]:
            score = min(score, alpha_beta(copie, next, alpha, beta, profondeur+1))
            if(score <= alpha):
                return score
            beta = min(beta, score)

    return score

def decision(jeu, coups):
    """ jeu*List[coup] -> coup
        retourne le coup dont le score correspond au score d’évaluation maximal
        de la liste de coups passée en paramètre
    """
    global val_tab
    if(jeu[1] == 1):
        val_tab = [[10,20,30,40,50,60],[60,50,40,30,20,10]]
    else :
        val_tab = [[60,50,40,30,20,10],[10,20,30,40,50,60]]

    scoreMax = -INF
    global joueur
    joueur = jeu[1]

    global scoreAvant
    scoreAvant = jeu[4]

    alpha = -INF
    beta = INF

    for coup in coups:
        score = alpha_beta(jeu, coup, alpha, beta, 1)
        if(score > alpha):
            alpha = score
            coupMax = coup
    return coupMax


def saisieCoup(jeu):
    return decision(jeu, game.getCoupsValides(jeu))
