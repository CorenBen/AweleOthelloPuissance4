#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    estim = -2
    liscoup = game.getCoupsValides(jeu)
    fauxjeu = game.getCopieJeu(jeu)
    profondeur = 1

    for i in range(len(liscoup)):
        if(estim < evaluation(fauxjeu,liscoup[i],profondeur)):
            estim = evaluation(fauxjeu,liscoup[i],profondeur)
            coupScore = liscoup[i]
    return coupScore

def evaluation(jeu,coup,profondeur):
    """jeu * [nat nat] * nat -> float
        Retourne le score d'evalution d'un etat de jeu
    """
    jeton = jeu[0][coup[0]][coup[1]]
    case = coup
    score = 0
    jeu[0][coup[0]][coup[1]]=0

    while(jeton > 0):
        case = game.game.nextCase(jeu,case)
        if(coup != case):
            jeu[0][case[0]][case[1]]+=1
            jeton-=1

    ligne = case[0]
    colonne = case[1]

    while(game.game.peutManger(jeu,[ligne,colonne])):
        if(game.game.adversaireAffame(jeu)):
            return -1
        score += jeu[0][ligne][colonne]
        jeu[0][ligne][colonne]=0
        if(ligne==0):
            if(colonne==0):
                ligne+=1
            else:
                colonne-=1
        else:
            if(colonne==5):
                ligne-=1
            else:
                colonne+=1
    return score
