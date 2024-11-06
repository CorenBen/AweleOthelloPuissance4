#!/usr/bin/env python
# -*- coding: utf-8 -*-

def initialiseJeu():
    """ void -> jeu
    """
    plateau = [[0 for i in range(8)] for x in range(8)]
    plateau[3][3] = 1
    plateau[4][4] = 1
    plateau[3][4] = 2
    plateau[4][3] = 2
    jeu = [plateau, 1, None, [], [2, 2]]
    return jeu


def coupValide(jeu, c):
    """ jeu * [nat nat] -> List[case]
        Retourne True si le coup est valide, c'est à dire que la case est vide et qu'elle fait gagner au moins une piece
    """
    if jeu[0][c[0]][c[1]] != 0 or len(pieceManger(jeu, c)) == 1:
        return False

    return True


def pieceManger(jeu, c, coupValide = True):
    """ jeu * [nat nat] -> List[case]
        Retourne la liste de piece manger suite à un coup
    """
    listManger = [c]
    listDir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1,-1), (1, -1), (-1, 1)]

    for dir in listDir:                                 #Test sur les différentes direction possibles
        listMangerDir = []                  #Piece manger dans une direction
        pieceAdvRencontrer = False          #Piece adverse rencontrer ou non
        tmp = [c[0]+dir[0], c[1]+dir[1]]    #Position dans la direction donnée

        while tmp[0] >= 0 and tmp[0] < 8 and tmp[1] >= 0 and tmp[1] < 8:
            if pieceAdvRencontrer:                      #Test si on a deja rencontre une piece adverse
                if jeu[0][tmp[0]][tmp[1]] == jeu[1]:
                    listManger += listMangerDir         #On rencotre une de nos pieces, les pieces adverse sont manger
                    if coupValide:
                        return listManger
                    break
                if jeu[0][tmp[0]][tmp[1]] == 0:
                    break                               #On tombe sur une case vide, on sort de la boucle
            else:
                if jeu[0][tmp[0]][tmp[1]] == 0 or jeu[0][tmp[0]][tmp[1]] == jeu[1]:
                    break                               #Si on tombe sur une case vide ou une de nos piece direct, on sort de la boucle
                pieceAdvRencontrer = True

            listMangerDir.append((tmp[0], tmp[1]))
            tmp[0], tmp[1] = tmp[0]+dir[0], tmp[1]+dir[1]   #Deplacement dans la direction dir
    return listManger


def listeCoupsValides(jeu):
    """ jeu * [nat nat] -> List[coup]
	   Retourne la liste des coups valides selon l'etat du jeu. Un coup est valide si:
		  - La case correspondant au coup appartient bien au joueur courant
		  - La case permet au joueur de manger un pion adverse
    """
    coupsValides = []

    for ligne in range(8):
        for colonne in range(8):
            if coupValide(jeu, (ligne, colonne)):       #Test la validite du coup
                coupsValides.append((ligne, colonne))

    return coupsValides


def joueCoup(jeu, c):
    """ jeu * [nat nat] -> jeu
        Joue le coup c donnee
    """
    if c == None:
        jeu[2] = None
        if jeu[1] == 1:
            jeu[1] = 2
        else:
            jeu[1] = 1
        return jeu

    joueur = jeu[1]
    manger = pieceManger(jeu, c, False)

    for (ligne, colonne) in manger:
        jeu[0][ligne][colonne] = joueur     #Manger les pièces

    jeu[4][joueur-1] += len(manger)
    if joueur == 1:
        jeu[4][1] -= len(manger)-1
        jeu[1] = 2
    else:
        jeu[4][0] -= len(manger)-1
        jeu[1] = 1

    jeu[2] = None
    jeu[3].append(c)

    return jeu


def finJeu(jeu):
    """ jeu -> bool
        Retourne True si le jeu est fini, le joueur n'a plus de coups valides
    """
    if len(jeu[3]) == 60:
        True
    if listeCoupsValides(jeu) == []:
        if jeu[1] == 1:
            jeu[1] = 2
            if listeCoupsValides(jeu) == []:
                jeu[1] = 1
                return True
            else:
                jeu[1] = 1
                return False
        else:
            jeu[1] = 1
            if listeCoupsValides(jeu) == []:
                jeu[1] = 2
                return True
            else:
                jeu[1] = 2
                return False
