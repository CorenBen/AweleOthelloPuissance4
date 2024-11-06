#!/usr/bin/env python
# -*- coding: utf-8 -*-

#jeton: nat
#ligne2 : nat
#colonne2 : nat

#### MODIF
#### Ajout de jeu à toutes les fonctions
#### plateau -> jeu[0]
#### [ligne[colonne]] -> [ligne][colonne]

#### Fonction Ajouter
#### peutManger
#### nextCase
#### adversaireAffame
#### listeCoupsValides

fin = False

def initialiseJeu():
	""" void -> jeu
	Créé le plateau de jeu et le jeu
	"""
	plateau = [[0 for i in range(7)] for x in range(6)]
	jeu = [plateau, 1, None, [], [0, 0]]
	return jeu


def nonVide(jeu, ligne, colonne):
	""" void -> bool
	Retourne True si la case contient un jeton
	"""
	return jeu[0][ligne][colonne] != 0

def listeCoupsValides(jeu):
	""" jeu->List[coup]
		Retourne la liste des coups valides.
	"""
	listValide = []

	for colonne in range(7):
		for ligne in range(5,-1,-1):
			if not nonVide(jeu, ligne, colonne):
				listValide.append((ligne, colonne))
				break
	return listValide

def verifCoupfinal(jeu, ligne, colonne):
	"""jeu*nat*nat*plateau*Pair[nat nat] -> void
	Vérifie l'emplacement du coup final du joueur, s'il y a quatre jetons alignés la partie se termine
	"""
	if((ligne-1, colonne) in jeu[3]):
		if((ligne-2, colonne) in jeu[3] and jeu[0][ligne-1][colonne] == jeu[1]):
			if((ligne-3, colonne) in jeu[3] and jeu[0][ligne-2][colonne] == jeu[1]):
				return jeu[0][ligne-3][colonne] == jeu[1]

	if((ligne-1, colonne-1) in jeu[3]):
		if((ligne-2, colonne-2) in jeu[3] and jeu[0][ligne-1][colonne-1] == jeu[1]):
			if((ligne-3, colonne-3) in jeu[3] and jeu[0][ligne-2][colonne-2] == jeu[1]):
				return jeu[0][ligne-3][colonne-3] == jeu[1]

	if((ligne, colonne-1) in jeu[3]):
		if((ligne, colonne-2) in jeu[3] and jeu[0][ligne][colonne-1] == jeu[1]):
			if((ligne, colonne-3) in jeu[3] and jeu[0][ligne][colonne-2] == jeu[1]):
				return jeu[0][ligne][colonne-3] == jeu[1]

	if((ligne+1, colonne-1) in jeu[3]):
		if((ligne+2, colonne-2) in jeu[3] and jeu[0][ligne+1][colonne-1] == jeu[1]):
			if((ligne+3, colonne-3) in jeu[3] and jeu[0][ligne+2][colonne-2] == jeu[1]):
				return jeu[0][ligne+3][colonne-3] == jeu[1]

	if((ligne+1, colonne) in jeu[3]):
		if((ligne+2, colonne) in jeu[3] and jeu[0][ligne+1][colonne] == jeu[1]):
			if((ligne+3, colonne) in jeu[3] and jeu[0][ligne+2][colonne] == jeu[1]):
				return jeu[0][ligne+3][colonne] == jeu[1]

	if((ligne+1, colonne+1) in jeu[3]):
		if((ligne+2, colonne+2) in jeu[3] and jeu[0][ligne+1][colonne+1] == jeu[1]):
			if((ligne+3, colonne+3) in jeu[3] and jeu[0][ligne+2][colonne+2] == jeu[1]):
				return jeu[0][ligne+3][colonne+3] == jeu[1]

	if((ligne, colonne+1) in jeu[3]):
		if((ligne, colonne+2) in jeu[3] and jeu[0][ligne][colonne+1] == jeu[1]):
			if((ligne, colonne+3) in jeu[3] and jeu[0][ligne][colonne+2] == jeu[1]):
				return jeu[0][ligne][colonne+3] == jeu[1]

	if((ligne-1, colonne+1) in jeu[3]):
		if((ligne-2, colonne+2) in jeu[3] and jeu[0][ligne-1][colonne+1] == jeu[1]):
			if((ligne-3, colonne+3) in jeu[3] and jeu[0][ligne-2][colonne+2] == jeu[1]):
				return jeu[0][ligne-3][colonne+3] == jeu[1]



def affichePlateau(jeu):
	"""jeu -> void
	Affiche le plateau de jeu
	"""
	for i in (7):
		for j in range(6):
			print(jeu[0][i][j],end=' ')
		print("\n")

def joueCoup(jeu, c):
	"""jeu * [nat nat] -> jeu
	Joue le coup c donné
	"""
	if distribue(jeu,c) :
		if jeu[1] == 1:
			jeu[1] = 2
		else:
			jeu[1] = 1

		jeu[2] = listeCoupsValides(jeu)
		jeu[3].append(c)

	return jeu

def distribue(jeu,c):
	""" jeu * Pair[nat nat] -> void
	Egraine nb graines (dans le sens inverse des aiguilles d'une montre) en partant de la case suivant la case suivant celle pointee par cellule,
	puis mange ce qu'on a le droit de manger
	Pseudo-code :
		- Distribution des graines dans le sens inverse des aiguilles d'une montre en evitant la case de depart (si nb>=12, on nourrit plusieurs fois les memes cases)
		- Parcours du plateau dans le sens inverse tant qu'on peut manger des graines
	Note: on egrene pas dans la case de depart si on a fait un tour
	Note2: On ne mange rien si le coup affame l'adversaire
	"""
	case = c
	print(c)
	if nonVide(jeu,case[0],case[1]) :
		print('Coup invalide -> Case déjà prise')
		print('Veuiller rééssayer')
		return False
	else :
		jeu[0][case[0]][case[1]]=jeu[1]
	return True

