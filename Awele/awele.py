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

def initialiseJeu():
	""" void -> jeu
	Créé le plateau de jeu et le jeu
	"""
	plateau = [[4 for i in range(6)] for x in range(2)]
	jeu = [plateau, 1, None, [], [0, 0]]
	return jeu


def nonVide(jeu, ligne, colonne):
	""" void -> bool
	Retourne True si la case contient des billes
	"""
	return jeu[0][ligne][colonne] != 0


def peutManger(jeu, c):
	"""  jeu * Pair[nat nat] -> bool
	Retourne vrai si on peut manger le contenu de la case:
		- c est une case appartenant a l'adversaire du joueur courant
		- La case contient 2 ou 3 graines
	"""
	if((abs(jeu[1]-2) == c[0])):
		return jeu[0][c[0]][c[1]] == 2 or jeu[0][c[0]][c[1]] == 3
	return False


def nextCase(jeu, case, inv=True):
	""" jeu*Pair[nat nat]->Pair[nat nat]
		Retourne la prochaine case sur le plateau, dans le sens inverse des aiguilles d'une montre si inv est vrai, dans le sens des aiguilles d'une montre sinon
	"""
	if inv:
		if case[0] == 0:
			if case[1] == 0:
				return (1, 0)
			else:
				return (0, case[1]-1)
		else:
			if case[1] == 5:
				return (0, 5)
			else:
				return (1, case[1]+1)
	else:
		if case[0] == 0:
			if case[1] == 5:
				return (1, 5)
			else:
				return (0, case[1]+1)
		else:
			if case[1] == 0:
				return (0, 0)
			else:
				return (1, case[1]-1)

def verifCoupfinal(jeu, ligne, colonne, plateau, score):
	"""jeu*nat*nat*plateau*Pair[nat nat] -> void
	Vérifie l'emplacement du coup final du joueur, s'il y a deux billes elles sont retirés et ajoutés à son score et on vérifie la case précédente. Si l'adversaire est affamé, restitue le plateau et remet les scores initiaux
	"""
	if(adversaireAffame(jeu)):
		jeu[0] = plateau
		jeu[4] = score


	if(peutManger(jeu,[ligne,colonne])):
		jeu[4][jeu[1]-1] += jeu[0][ligne][colonne]
		jeu[0][ligne][colonne]=0
		if(ligne==0):
			if(colonne==0):
				verifCoupfinal(jeu, ligne+1, colonne, plateau, score)
			else:
				verifCoupfinal(jeu, ligne, colonne-1, plateau, score)
		else:
			if(colonne==5):
				verifCoupfinal(jeu, ligne-1, colonne, plateau, score)
			else:
				verifCoupfinal(jeu, ligne, colonne+1, plateau, score)


def adversaireAffame(jeu, inv=True):
	""" jeu -> bool
		Retourne si un des joueurs est affame ou non avec Joueur 1 = ligne 0 et Joueur 2 = ligne 1
	"""

	if inv:
		for colonne in range(6):
			if nonVide(jeu,abs(jeu[1]-2), colonne):
				return False
	else:
		for colonne in range(6):
			if nonVide(jeu,jeu[1]-1, colonne):
				return False

	return True

def listeCoupsValides(jeu):
	""" jeu->List[coup]
		Retourne la liste des coups valides selon l'etat du jeu. Un coup est valide si:
		- La case correspondant au coup appartient bien au joueur courant
		- La case correspondant au coup contient au moins une graine
		- Le coup nourrit l'adversaire si il est affame.
	"""
	listValide = []
	ligne = jeu[1]-1
	advAffame = adversaireAffame(jeu)

	for colonne in range(6):
		if nonVide(jeu, ligne, colonne):
			if advAffame:
				if ligne == 0:
					if jeu[0][ligne][colonne] > 5-colonne:
						listValide.append((ligne, colonne))
				else:
					if jeu[0][ligne][colonne] > colonne:
						listValide.append((ligne, colonne))
			else:
				listValide.append((ligne, colonne))

	return listValide


def finJeu(jeu):
	"""void -> bool
	Renvoie True si le nombre de billes est inférieur ou égal à 12
	"""
	if(listeCoupsValides(jeu) == []):
		return True
	jeton = 0
	for i in [0, 1]:
		for j in range(6):
			jeton+=jeu[0][i][j]
	return jeton<=12

def affichePlateau(jeu):
	"""jeu -> void
	Affiche le plateau de jeu
	"""
	for i in [0, 1]:
		for j in range(6):
			print(jeu[0][i][j],end=' ')
		print("\n")

def joueCoup(jeu, c):
	"""jeu * [nat nat] -> jeu
	Joue le coup c donné
	"""
	distribue(jeu,c)

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
	jeton = jeu[0][c[0]][c[1]]
	case = c
	jeu[0][c[0]][c[1]]=0

	while(jeton > 0):
		case = nextCase(jeu,case)
		if(c != case):
			jeu[0][case[0]][case[1]]+=1
			jeton-=1

	verifCoupfinal(jeu, case[0], case[1], jeu[0], jeu[4])
