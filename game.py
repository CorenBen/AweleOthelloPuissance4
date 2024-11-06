#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random
# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup:[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:[plateau nat List[coup] List[coup] List[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    copie = copy.deepcopy(jeu)
    getCoupsValides(copie)
    return copie

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return game.finJeu(jeu)

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    if jeu[1] == 1:
        return joueur1.saisieCoup(jeu)
    return joueur2.saisieCoup(jeu)


def getCoupsValides(jeu):
    """ jeu -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
    """
    if jeu[2] is None:
        list = game.listeCoupsValides(jeu)
        jeu[2] = list
    return jeu[2]

def getCoupsValidesP(jeu):

    if jeu[2] is None:
        list = game.listeCoupsValides(jeu)
        jeu[2] = list
        return jeu[2]
    else :
        return game.listeCoupsValides(jeu)

def coupValide(jeu,coup):
    """ jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
    """
    if (coup in getCoupsValides(jeu)):
        return True
    else:
        return False


def joueCoup(jeu,coup):
    """ jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    game.joueCoup(jeu, coup)


def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    return game.initialiseJeu()


def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    if jeu[4][0] == jeu[4][1]:
        return 0
    elif jeu[4][0] > jeu[4][1]:
        return 1
    else:
        return 2


def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer

         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    if (len(jeu[3]) != 0):
        print('Coup joue = {}'.format(getCoupsJoues(jeu)[len(jeu[3])-1]))
    print('Scores = {}'.format(getScores(jeu)))

    #affiche plateau
    nbLignes = getNbLignes(jeu)
    nbColonnes = getNbColonnes(jeu)

    print('Plateau:\n\n     ', end = '')
    for i in range(nbColonnes):
        print('|  {}  '.format(i), end='')

    for i in range(nbLignes):
        print('\n' + '------'*(nbColonnes+1))
        print('  {}  '.format(i), end = '')
        for x in range(nbColonnes):
            print('| {:-2}  '.format(jeu[0][i][x]), end = '')

    print('\nJoueur {}, a vous de jouer\n'.format(jeu[1]))

# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]

def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]


def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    if (jeu[1] == 1):
        jeu[1] = 2
    else:
        jeu[1] = 1

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return jeu[4][joueur]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return jeu[0][ligne][colonne]

def getNbLignes(jeu):
    """ jeu -> int
        Retourn le nombre de ligne de plateau
    """
    return len(jeu[0])

def getNbColonnes(jeu):
    """ jeu -> int
        Retourn le nombre de collone de plateau
    """
    return len(jeu[0][0])

def setCaseVal(jeu, ligne, colonne, val):
    """ jeu*int*int*nat -> void
        Met val dans la case plateau[ligne][colonne]
    """
    jeu[0][ligne][collonne] = val

def addCaseVal(jeu, ligne, colonne, val):
    """ jeu*int*int*nat -> void
        Ajoute val à la case plateau[ligne][colonne]
    """
    jeu[0][ligne][colonne]

def addScore(jeu, joueur, score):
    """ jeu*nat*int -> int
        Ajoute score au Score du joueur
    """
    jeu[4][jeu[1]] += score


def unMatch():
    """ void -> nat
        Simule un match et renvoie le joueur gagnant
    """
    jeu = initialiseJeu()

    for i in range(4):
        coup = random.choice(getCoupsValides(jeu))
        joueCoup(jeu, coup)

    while(not(finJeu(jeu))):
        if getCoupsValides(jeu) != []:
            coup = saisieCoup(jeu)
        else:
            coup = None
        joueCoup(jeu, coup)


    affiche(jeu)
    winner = getGagnant(jeu)
    return winner

def verifCoupfinal(jeu, l, c):
    return game.verifCoupfinal(jeu,l,c)

def simulation(n):
    """ void -> void
        Simule n match et affiche les resultats de la simulation
    """
    stat = [0, 0, 0]

    for i in range(n):
        stat[unMatch()] += 1

    return stat

def finJeuP():
    return game.finJeu()