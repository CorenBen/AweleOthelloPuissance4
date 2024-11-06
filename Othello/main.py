#!/usr/bin/env python
# -*- coding: utf-8 -*-
import othello
import sys
import time
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
import joueur_random
import joueur_horizon1
import joueur_MinMax
import joueur_alpha_beta
import joueur_newHorizon1
game.joueur1 = joueur_MinMax
game.joueur2 = joueur_horizon1

#n = int(input("Nombre de simulation:"))
n = 100
stat1 = game.simulation(int(n/2))

game.joueur1, game.joueur2 = game.joueur2, game.joueur1

stat2 = game.simulation(int(n/2))


nul = (stat1[0] + stat2[0])/n*100
v1 = (stat1[1] + stat2[2])/n*100
v2 = (stat1[2] + stat2[1])/n*100

print('Joueur1: winrate en jouant en premier: {}%'.format(stat1[1]*100./(stat1[0]+stat1[1]+stat1[2])))
print('Joueur2: winrate en jouant en premier: {}%'.format(stat2[1]*100./(stat2[0]+stat2[1]+stat2[2])))
print('sur {} parties, {}% match nul, {}% victoire du joueur1, {}% victoire du joueur2'.format(n, nul, v1, v2))
