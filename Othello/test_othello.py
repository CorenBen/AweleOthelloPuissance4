#!/usr/bin/env python
# -*- coding: utf-8 -*-
import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_random
game.joueur1=joueur_random
game.joueur2=joueur_random

#### Test sur une partie aléatoire

jeu = game.initialiseJeu()

assert game.finJeu(jeu) == False    #Test que le jeu n'est pas fini des le debut

coup = game.saisieCoup(jeu)
assert coup in jeu[2]       #Test si le coup aleatoire tire est bien valide

game.joueCoup(jeu, coup)
assert jeu[4] == [4, 1]     #Test le comptage des scores apres un coup joué

nbcoup = 1

while(not(game.finJeu(jeu))):
    coup = game.saisieCoup(jeu)
    game.joueCoup(jeu, coup)
    nbcoup += 1

assert nbcoup <= 60         #Test qu'il n'y a pas plus de coup joue que possible
assert game.finJeu(jeu) == True     #Test la finition du jeu

score1, score2 = 0, 0
for ligne in jeu[0]:
    for elem in ligne:
        if elem == 1:
            score1 += 1
        elif elem == 2:
            score2 += 1

assert jeu[4] == [score1, score2]   #Test le comptage des scores




jeu[0] = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 2, 0, 2, 0],
          [0, 0, 0, 0, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 2, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]


jeu[1] = 1
game.joueCoup(jeu, (4, 4))

plateau = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

assert jeu[0] == plateau           #Test manger sur plusieur direction en meme temps
assert game.finJeu(jeu)
