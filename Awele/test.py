#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
print(os.getcwd())
os.chdir("/Users/coren/Desktop/RepEtudiants/Awele")
import awele
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_random
game.joueur1=joueur_humain
game.joueur2=joueur_random
import random

jeu = game.game.initialiseJeu()
plateaubase = [[4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4]]
jeu[1] = 1

#Cas de figure 1 : On verifie que le coup a ete joue
plateaucopie = [[4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4]]
jeu[0] = plateaucopie
game.joueCoup(jeu,game.joueur2.saisieCoup(jeu))
assert(plateaubase != plateaucopie)

#Cas de figure 2 : On verifie que la recuperation de point a ete annule si un camp est affame et que le plateau est inchange
plateaucopie = [[2,0,0,0,0,0],[0,0,0,0,0,0]]
score = jeu[4]
game.game.verifCoupfinal(jeu,0,0,plateaucopie,jeu[4])
assert(plateaucopie == [[2,0,0,0,0,0],[0,0,0,0,0,0]])
assert(score == jeu[4])

#Cas de figure 3 : On verifie que la partie se finit bien
plateaucopie = [[2,0,0,0,0,0],[0,0,0,0,0,0]]
jeu[0] = plateaucopie
assert(game.finJeu(jeu) == True)

#Cas de figure 4 : On verifie que la fonction nextCase marche sur les bords
plateaucopie = [[4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4]]
jeu[0] = plateaucopie
case = (0,0)
assert(game.game.nextCase(jeu,case)==(1,0))
case = (1,5)
assert(game.game.nextCase(jeu,case)==(0,5))

#Cas de figure 5 : On verifie que la fonction saisieCoup de joueur_random donne bien des coups valides
plateaucopie = [[0, 0, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4]]
jeu[0] = plateaucopie
for i in range(20):
    assert(joueur_random.saisieCoup(jeu) in game.getCoupsValides(jeu))