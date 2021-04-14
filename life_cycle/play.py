# coding: utf-8

import json
import sys
from os import path
sys.path.append('../')
from game.play import *


######################### FONCTION PARTIE 3 #########################


def save_game(partie):

	"""
		Sauvegarde une partie en cours dans le fichier game_saved.json
	"""

	#On ouvre le fichier game_saved.json dans la variable save en mode écriture
	save = open ("E:/jeu_threes/life_cycle/game_saved.json","w")
	#On copie la partie dans save donc dans le fichier game_saved.json
	json.dump(partie, save)
	#On ferme le fichier game_saved.json
	save.close()


def restore_game():

	"""
		Restaure et retourne une partie sauvegardée dans le
		fichier "game_saved.json", ou retourne une nouvelle partie si aucune partie n'est sauvegardée
	"""

	#On ouvre le fichier game_saved.json dans la variable restore_f en mode lecture
	restore_f = open("E:/jeu_threes/life_cycle/game_saved.json","rt")
	#On copie le contenue dans le fichier game_saved.json dans la variable game_json
	game_json = restore_f.read()
	#On ferme le fichier game_saved.json
	restore_f.close()
	#Si game_json est vide
	if len(game_json) == 0:
		#Alors on reourne une nouvelle partie
		return create_new_play()
	#On affecte la partie contenue dans la variable game_json a la variable game 
	game = json.loads(game_json)
	#On retourne la partie donc game
	return game


#####################################################################


