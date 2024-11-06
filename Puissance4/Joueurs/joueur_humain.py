#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coupValide = game.getCoupsValides(jeu)

    if len(coupValide) > 0:
        (ligne, colonne) = input("Veuillez insérer votre coup:").split()
        (ligne, colonne) = (int(ligne), int(colonne))
        while ((ligne, colonne) not in coupValide):
            print('({}, {}) n\'est pas un coup valide.'.format(ligne, colonne))
            (ligne, colonne) = input("Veuillez insérer votre coup:").split()
            (ligne, colonne) = (int(ligne), int(colonne))


    return (ligne, colonne)

