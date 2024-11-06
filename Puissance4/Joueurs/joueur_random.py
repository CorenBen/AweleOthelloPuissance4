#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup aleatoire joue
    """
    if(game.getCoupsValidesP(jeu)) == []:
        return None
    return random.choice(game.getCoupsValidesP(jeu))

