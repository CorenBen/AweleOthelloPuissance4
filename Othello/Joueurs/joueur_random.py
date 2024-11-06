#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup valide aléatoire
    """
    return random.choice(jeu[2])
