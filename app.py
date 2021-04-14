# coding: utf-8

import json
#import sys
#rom os import path
#sys.path.append('tiles/')
from tiles.tiles_moves import *
from tiles.tiles_acces import *
#sys.path.append('game/')
from game.play import *
#sys.path.append('ui/')
from ui.play_display import *
from ui.user_entries import *
from life_cycle.play import *
from curses import *


def threes():

	"""
		Cette fonction doit permettre d'enchainer les partie au jeu threes,
		de reprendre une partie sauvegarder et de sauvegarder une partie en cours
	"""
	
	#Boucle infini jusqu'a un return
	while True:
		#On affiche le menu simple, l'utilisateur fait son choix
		choix = get_user_menu(None)
		#On met une condition pour pouvoir sortir de la boucle quand on le veut
		condition = True
		while condition:
			#Si le joueur veut commencer une nouvelle partie
			if choix == 'N':
				#On lance cycle_play sans partie en parametres pour creer la nouvelle
				partie = cycle_play(None)
			#Si le joueur veut charger une partie sauvegarder
			elif choix == 'L':
				#On lance cycle_play avec la partie sauvegarder en parametres
				partie = cycle_play(restore_game())
			#Si le joueur veut sauvegarder sa partie
			elif choix == 'S':
				#On sauvegarde la partie a laquelle il etait entrain de jouer
				save_game(partie)
			#Si le joueur veut continuer sa partie
			elif choix == 'C':
				#On lance cycle_play avec la partie a laquelle il jouer
				partie = cycle_play(partie)
			#Si le joueur veut quitter le jeu
			elif choix == 'Q':
				#On quitte la fonction
				return
			#Si la partie est fini donc partie = True car cycle_play return True 
			if partie == True:
				#On sors de la boucle et on affiche le menu simple
				condition = False
			#Sinon la partie n'est pas finie alors le joueur a demander le menu  
			else:
				#On affiche donc le menu de pause
				choix = get_user_menu(partie)
		


threes()

#python E:\jeu_threes\app.py
