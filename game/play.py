# coding: utf-8

import sys
from os import path
sys.path.append('../')
from tiles.tiles_moves import *    
from tiles.tiles_acces import *
from ui.user_entries import *   
from curses import *     


######################### FONCTION PARTIE 1 #########################



def init_play():

	"""
		Retourne un plateau correspondant a une nouvelle partie
		Une nouvelle partie est un dictionnaire avec les clefs et valeurs suivantes :
		- 'n' = 4
		- 'nb_cases_libre' = 16 au départ
		- 'tiles' = tableau de 4*4 cases initialisés a 0
	"""

	#Création dico du plateau
	plateau = {}
	#On rentre la taille du plateau
	plateau["n"] = 4
	#Puis le nombres de cases libres (16 car toutes les cases sont libre)
	i = 1
	while i < plateau['n']*plateau['n']:
		i += 1
	plateau["nombres_cases_libres"] = i
	#On crée un tableau de 16 cases vide
	tab_plateau = []
	i = 0
	while i < plateau["nombres_cases_libres"]:
		tab_plateau.append(0)
		i += 1
	#Enfin on rentre le tableau constiter de 16 cases vide
	plateau["tiles"] = tab_plateau
	#Et on retourne le plateau
	return plateau

def is_game_over(plateau):

	"""
		Retourne True si la partie est terminée, False sinon
		Une partie est terminé si on ne peut plus faire de mouvement et qu'il n'y a plus de cases libres
	"""

	n = get_nb_empty_rooms(plateau)
	#Si il n'y a plus de cases libres le jeux est possiblement fini 
	if n == 0:
		#On vérifie qu'on ne peut pas faire de mouvements sur les lignes
		num_lig = 0
		while num_lig < 4 : 
			i = 0
			while i < 3:
				t1 = plateau['tiles'][4*num_lig + i]
				t2 = plateau['tiles'][4*num_lig + (i+1)]
				#Si on peut faire un mouvements le jeux n'est pas finie donc on return False
				if  (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2) or (t1 == 2 and t2 == 1):
					return False
				i += 1
			num_lig += 1
		#On vérifie qu'on ne peut pas faire de mouvements sur les colonnes
		num_col = 0
		while num_col < 4:
			i = 3
			while i > 0 : 
				t1 = plateau['tiles'][4*i + num_col]
				t2 = plateau['tiles'][4*(i-1) + num_col]
					#Si on peut faire un mouvements le jeux n'est pas finie donc on return False
				if (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2) or (t1 == 2 and t2 == 1):
					return False
				i -= 1
			num_col += 1
		return True
	return False

def get_score(plateau):

	"""
		Retourne le score du plateau
		Le score du plateau est l'addition de la valeur de chaque tuile sur le plateau
	"""

	#On initialise le score a 0
	score = 0
	i = 0
	#On parcours les tuiles du tableau
	while i < len(plateau["tiles"]):
		#On ajoute la valeur de chaque tuile au score
		score += plateau["tiles"][i]
		i += 1
	#On return le score
	return score


#####################################################################


######################### FONCTION PARTIE 3 #########################



def create_new_play():

	"""
		Créer et retourne un nouvelle partie qui contient :
		- 'plateau' = un plateau contenant deux tuiles 1 & 2
		- 'next_tiles' = prochaine tuiles du plateau
		- 'score' = 3 au début
	"""

	#On crée un nouveau plateau vide
	p = init_play()
	#On y ajoute les deux tuiles correspondant au mode init de get_next_alea_tiles
	put_next_tiles(p, get_next_alea_tiles(p, 'init'))
	#On crée le dico de la partie
	play = {}
	#On y ajoute le plateau de jeux précédemment créer
	play['plateau'] = p
	#On y ajoute la prochaine tuiles avec la fonction get_next_alea_tiles
	play['next_tile'] = get_next_alea_tiles(p, 'encours')
	#Et on y ajoute le score de la partie 
	play['score'] = get_score(p)
	#On retourne ce nouveau dico 
	return play

def cycle_play(partie):

	"""
		Permet de jouer a Threes,
		prends en parametres la partie en cours ou None sinon,
		retourne True si la partie est terminée, False si le menu est demandé

	"""

	#Si il n'y a aucune partie en cours
	if partie is None:
		#On crée une nouvelles parties
		partie = create_new_play()
		#Avec un boucle infinie on simule la partie
		while True:
			#On extrait le plateau de jeux
			plateau = partie['plateau']
			#On l'affiche
			full_display(plateau)
			#On prend la valeur de la prochaine tuile
			tile = partie['next_tile']['0']['val']
			#On l'affiche
			print("Prochaine tuile :", tile)
			#On affiche le score
			print("Score : ", partie['score'])
			#On demande au joueur le mouvement qu'il veut faire
			move = get_user_move()
			#Si il demande le menu
			if move == 'm':
				#On return la partie et non pas False car celle ci a était creer dans la fonction
				#et si on veut la save ou la reprendre il faut la retourner
				return partie
			#Sinon on execute le mouvement demander sur le tableau
			play_move(plateau, move)
			#Si il reste au moins une case vide on cree la prochaine tuiles
			#Cette partie permet d'avoir une tuiles avec la meme valeurs que celle qu'afficher au joueur mais avec les coordonnées d'une case libres aprés avoir jouer son coup
			if get_nb_empty_rooms(partie['plateau']) > 0:
				#On la cree mais on garde seulement son emplacement
				partie['next_tile'] = get_next_alea_tiles(plateau, 'encours')
				#Et on change sa valeur par la valeur indiquer au joueur pendant le jeux
				partie['next_tile']['0']['val'] = tile
				#Ensuite on insére la tuile dans le plateau
				put_next_tiles(plateau, partie['next_tile'])
			#On met a jour le score
			partie['score'] = get_score(partie['plateau'])
			#Si aprés avoir insérer la tuiles il reste au moins une case vide
			if get_nb_empty_rooms(partie['plateau']) > 0:
				#On cree donc la prochaine tuile dont on ne gardera que le valeur
				partie['next_tile'] = get_next_alea_tiles(plateau, 'encours')
			#On vérifie si la partie est terminé
			if is_game_over(plateau):
				#On utilise curses pour afficher l'ecran de fin de jeux
				win1 = curses.initscr()
				maxY, maxX = win1.getmaxyx()
				#cette fonction permet a l'utilisateur de ne pas avoir a appuyer sur entrer pour valider
				curses.cbreak()
				win1.border('|', '|', '-', '-', '+', '+', '+', '+')
				win1.addstr(int(maxY/2)-2, int(maxX/2)-10, "GAME OVER", curses.A_STANDOUT)
				#On affiche le score
				win1.addstr(int(maxY/2), int(maxX/2)-10, "SCORE : {}".format(partie['score']), curses.A_STANDOUT)
				#Et pour continuer a jouer il doit appuyer sur la touche espace
				win1.addstr(int(maxY/2)+10, int(maxX/2)-20, "APPUYER SUR ESPACE POUR CONTINUER", curses.A_BLINK)
				#On controle presser la touche avec une saisie controler
				suite = win1.getkey()
				while suite != ' ':
					suite = win1.getkey()
				win1.refresh()
				curses.nocbreak()
				win1.clear()
				curses.endwin()
				#La partie est finie donc on return True
				return True
	#Si une partie de jeux est deja en cours
	else:
		#Avec un boucle infinie on simule la partie
		while True:
			#On extrait le plateau de jeux
			plateau = partie['plateau']
			#On l'affiche
			full_display(plateau)
			#On prend la valeur de la prochaine tuile
			tile = partie['next_tile']['0']['val']
			#On l'affiche
			print("Prochaine tuile :", tile)
			#On affiche le score
			print("Score : ", partie['score'])
			#On demande au joueur le mouvement qu'il veut faire
			move = get_user_move()
			#Si il demande le menu
			if move == 'm':
				#On return la partie et non pas False car celle ci a était creer dans la fonction
				#et si on veut la save ou la reprendre il faut la retourner
				return partie
			#Sinon on execute le mouvement demander sur le tableau
			play_move(plateau, move)
			#Si il reste au moins une case vide on cree la prochaine tuiles
			#Cette partie permet d'avoir une tuiles avec la meme valeurs que celle qu'afficher au joueur mais avec les coordonnées d'une case libres aprés avoir jouer son coup
			if get_nb_empty_rooms(partie['plateau']) > 0:
				#On la cree mais on garde seulement son emplacement
				partie['next_tile'] = get_next_alea_tiles(plateau, 'encours')
				#Et on change sa valeur par la valeur indiquer au joueur pendant le jeux
				partie['next_tile']['0']['val'] = tile
				#Ensuite on insére la tuile dans le plateau
				put_next_tiles(plateau, partie['next_tile'])
			#On met a jour le score
			partie['score'] = get_score(partie['plateau'])
			#Si aprés avoir insérer la tuiles il reste au moins une case vide
			if get_nb_empty_rooms(partie['plateau']) > 0:
				#On cree donc la prochaine tuile dont on ne gardera que la valeur
				partie['next_tile'] = get_next_alea_tiles(plateau, 'encours')
			#On vérifie si la partie est terminé
			if is_game_over(plateau):
				#On utilise curses pour afficher l'ecran de fin de jeux
				win1 = curses.initscr()
				maxY, maxX = win1.getmaxyx()
				#cette fonction permet a l'utilisateur de ne pas avoir a appuyer sur entrer pour valider
				curses.cbreak()
				win1.border('|', '|', '-', '-', '+', '+', '+', '+')
				win1.addstr(int(maxY/2)-2, int(maxX/2)-9, "GAME OVER", curses.A_STANDOUT)
				#On affiche le score
				win1.addstr(int(maxY/2), int(maxX/2)-10, "SCORE : {}".format(partie['score']), curses.A_STANDOUT)
				#Et pour continuer a jouer il doit appuyer sur la touche espace
				win1.addstr(int(maxY/2)+10, int(maxX/2)-20, "APPUYER SUR ESPACE POUR CONTINUER", curses.A_BLINK)
				#On controle presser la touche avec une saisie controler
				suite = win1.getkey()
				while suite != ' ':
					suite = win1.getkey()
				win1.refresh()
				curses.nocbreak()
				win1.clear()
				curses.endwin()
				#La partie est finie donc on return True
				return True


#####################################################################
