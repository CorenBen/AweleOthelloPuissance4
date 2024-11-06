#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
print(os.getcwd())
os.chdir("/Users/coren/Desktop/RepEtudiants/Puissance4")
import p4
sys.path.append("..")
import game
game.game=p4
sys.path.append("./Joueurs")
import joueur_humain
import joueur_random
import joueur_minmax
game.joueur1=joueur_random
game.joueur2=joueur_minmax
import random

minmax = 0
for i in range(100):
    finjeu = False
    jeu = game.initialiseJeu()
    while(not(finjeu)):
        if game.getCoupsValides(jeu) != []:
            coup = game.saisieCoup(jeu)
            game.joueCoup(jeu, coup)
            if(game.verifCoupfinal(jeu,coup[0],coup[1])):
                if(jeu[2]==0):
                    jeu[4]=[1,0]
                else :
                    jeu[4]=[0,1]
                finjeu = True
        else :
            finjeu = True
        game.affiche(jeu)

    winner = game.getGagnant(jeu)
    if winner == 2:
        minmax +=1
print(minmax)
