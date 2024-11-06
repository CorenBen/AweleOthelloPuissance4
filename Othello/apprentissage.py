#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random
import othello
import sys
import time
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_random
import joueur_horizon1
import joueur_alpha_beta
import joueur_apprentissage
game.joueur1 = joueur_apprentissage
game.joueur2 = joueur_alpha_beta
joueurParam = game.joueur1
oracle = joueur_alpha_beta

fichier = open("apprentissage.txt", "w")

params = [5,10,15]
joueurParam.params = params
alpha = 0.005

while(True):
    paramsPrec = copy.deepcopy(params)
    convergeParam = False
    jeu = game.initialiseJeu()

    for i in range(4):
        coup = random.choice(game.getCoupsValides(jeu))
    game.joueCoup(jeu, coup)

    while(not(game.finJeu(jeu))):
        if(game.getCoupsValides(jeu) != []):
            scoreOrac, opt, scoreOpt = oracle.getScoreCoup(jeu, jeu[2])
            scoreParam = joueurParam.getScoreCoup(jeu, jeu[2])
            scjOpt = joueurParam.estimation(jeu, opt)

            for i in range(len(jeu[2])):
                if(scoreOrac[i] < scoreOpt):
                    o = 0
                    s = 0
                    for param in params:
                        o += param * scjOpt
                        s += param * scoreParam[i]

                    if((o-s) < 1):
                        for j in range(3):
                            scjOpt = joueurParam.estimation(jeu, opt)
                            scjC = joueurParam.estimation(jeu, jeu[2][i])
                            params[j] -= alpha * (scjC - scjOpt)
                            joueurParam.params = params

        #Faire joueur les joueurs
        for i in range(2):
            if(game.getCoupsValides(jeu) != []):
                coup = game.saisieCoup(jeu)
            else:
                coup = None
            game.joueCoup(jeu, coup)

    fichier.write(str(params)+"\n")
    alpha -= alpha/10

    #Test de convergence (chacun des paramètre n'a qu'été modifié au maximum de 0.1)
    for i in range(3):
        if(abs(paramsPrec[i] - params[i]) > 1):
            convergeParam = False
            break
        convergeParam = True


    if(convergeParam):
        break

fichier.close()
