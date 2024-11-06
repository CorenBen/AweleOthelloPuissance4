#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

ProfondeurMax = 2
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

def minmax(jeu, coup, profondeur):
    """ jeu * coup * profondeur -> float
      Fonction récursive qui retourne un score d’utilité estimée pour un etat de jeu à partir d’appels de la fonction d’evaluation sur les feuilles de l’arbre (lorsque profondeur=pmax)
    """
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    coupValides = game.getCoupsValides(copie)

    if(game.verifCoupfinal(copie,coup[0],coup[1])):
        gagnant = game.getGagnant(copie)
        if(gagnant == joueur):
            return 100000000
        if(gagnant == 0):
            return -500
        return -100000000

    if(profondeur == ProfondeurMax):
        return evaluation(copie)

    if copie[1] == joueur:
        score = -INF
        for coupV in coupValides:
             score = max(score, minmax(copie, coupV, profondeur+1))
    else:
        score = INF
        for coupV in coupValides:
            score = min(score, minmax(copie, coupV, profondeur+1))

    return score


def decision(jeu, coups):
    """ jeu * List[coup] -> coup
       Retourne le coup dont le score correspond au score d’évaluation maximal de la liste de coups passée en paramètre
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


    for coup in coups:
        score = minmax(jeu, coup, 1)
        if score > scoreMax:
            scoreMax = score
            coupMax = coup

    return coupMax

def saisieCoup(jeu):
    return decision(jeu, game.getCoupsValides(jeu))
