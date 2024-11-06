#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Demande aux joueurs de saisir un coup valide et le retourne
    """
    (ligne, colonne) = input("Veuillez insérer votre coup:").split()
    (ligne, colonne) = (int(ligne), int(colonne))
    while ((ligne, colonne) not in jeu[2]):
        print('({}, {}) n\'est pas un coup valide.'.format(ligne, colonne))
        (ligne, colonne) = input("Veuillez insérer votre coup:").split()
        (ligne, colonne) = (int(ligne), int(colonne))

    return (ligne, colonne)
