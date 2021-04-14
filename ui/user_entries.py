# coding: utf-8
#include <curses.h>

import curses
import sys
from os import path
sys.path.append('../')
from game.play import *


######################### FONCTION PARTIE 3 #########################


def get_user_move():

	"""
		Saisi et retourne le coups joué (en minuscules) par le joueur parmi les choix :
		- 'h' = haut
		- 'b' = bas
		- 'g' = gauche
		- 'd' = droite
		- 'm' = menu
	"""

	#On lui demande ce qu'il veut faire
	print("Veuillez entrer votre prochain coup ==> h = haut ; b = bas ; g = gauche ; d = droite ; m = menu ")
	#Il rentre son coups
	#Il sera transformer en minuscules a chaques fois
	move = str(input()).lower()
	#On controle si la saisie est valable
	while move != 'h' and move != 'b' and move != 'g' and move != 'd' and move != 'm':
		#Si saisie non valable il doit rentrer un nouveau coups
		print("Saisie non valide veuillez saisir une seul lettres ==> h = haut ; b = bas ; g = gauche ; d = droite ; m = menu")
		move = str(input()).lower()
	#OOn return le coups choisi
	return move

def get_user_menu(partie):

	"""
		Saisi et retourne le choix du joueur (en majuscule) dans le menu simple ou le menu pause,
		il prend en parametres la partie si une partie est en cours (Menu pause) est None si aucune partie est en cours (Menu simple),
		il a le choix entre :
		- 'N' = Commencer une nouvelle partie
		- 'L' = Charger une partie
		- 'S' = Sauvegarder la partie en cours (si Menu pause)
		- 'C' = Reprendre la partie en cours (si Menu pause)
		- 'Q' = Terminer le jeu
	"""

	#Si aucune partie est en cours on fait un menu simple
	#3 choix possibles car il n'y a pas de partie en cours donc on ne peut pas sauvegarder et reprendre une partie
	if partie is None:
		#On crée une fenetre d'affichage qui fait la taille de la page par défaut
		win1 = curses.initscr()
		#On récuperes les coordonnées max de cette fenétres
		maxY, maxX = win1.getmaxyx()
		#curses.nocbreak permet de devoir appuyer sur entrée pour confirmer son choix
		curses.nocbreak()
		#On définit comment sont faites les bordures
		win1.border('|', '|', '-', '-', '+', '+', '+', '+')
		#On ajoutes les écritures voulu dans le menu simple 
		#Ces écritures sont au millieux graces au coordonnées maximum récuperer au préalable
		win1.addstr(1, int(maxX/2)-4, "MENU THREES", curses.A_UNDERLINE)
		win1.addstr(int(maxY/8), int(maxX/2)-20, "- N : Commencer une nouvelle partie", curses.A_STANDOUT)
		win1.addstr(int(maxY/8)+2, int(maxX/2)-20, "- L : Charger une partie       ", curses.A_BOLD)
		win1.addstr(int(maxY/8)+4, int(maxX/2)-20, "- Q : Terminez le jeu", curses.A_DIM)
		win1.addstr(int(maxY/8)+6, int(maxX/2)-20, "CHOISIR ET APPUYER SUR ENTREE : ", curses.A_BLINK)
		#On laisse l'utilisateur entrée son choix qui sera mit en majuscule automatiquement		
		choix = win1.getkey().upper()
		i = 2
		#Saisie controlée des choix disponibles
		while choix != 'N' and choix != 'L' and choix != 'Q':
			win1.addstr(int(maxY/8)+6, int(maxX/2)+13+i, " ", curses.A_BLINK)
			#On laisse l'utilisateur faire un autres choix
			choix = win1.getkey().upper()
			i += 1
		#On rafraichit la page pour tout afficher
		win1.refresh()
		#Puis on efface tout
		win1.clear()
		#Et on ferme la fenetre
		curses.endwin()
	#Si une partie est en cours alors le menu est un menu pause on a donc plus de possibilités
	#5 choix possibles
	else:
		#On crée une fenetre d'affichage qui fait la taille de la page par défaut
		win2 = curses.initscr()
		#On récuperes les coordonnées max de cette fenétres
		maxY, maxX = win2.getmaxyx()
		#curses.nocbreak permet de devoir appuyer sur entrée pour confirmer son choix
		curses.nocbreak()
		#On définit comment sont faites les bordures
		win2.border('|', '|', '-', '-', '+', '+', '+', '+')
		#On ajoutes les écritures voulu dans le menu pause
		#Ces écritures sont au millieux graces au coordonnées maximum récuperer au préalable
		win2.addstr(1, int(maxX/2)-8, "MENU PAUSE THREES", curses.A_UNDERLINE)
		win2.addstr(int(maxY/8), int(maxX/2)-20, "- N : Commencer une nouvelle partie", curses.A_STANDOUT)
		win2.addstr(int(maxY/8)+2, int(maxX/2)-20, "- L : Charger une partie", curses.A_BOLD)
		win2.addstr(int(maxY/8)+4, int(maxX/2)-20, "- S : Sauvegardez la partie en cours", curses.A_BOLD)
		win2.addstr(int(maxY/8)+6, int(maxX/2)-20, "- C : Reprendre la partie en cours", curses.A_BOLD)
		win2.addstr(int(maxY/8)+8, int(maxX/2)-20, "- Q : Terminez le jeu", curses.A_DIM)
		win2.addstr(int(maxY/8)+10, int(maxX/2)-20, "CHOISIR ET APPUYER SUR ENTREE : ", curses.A_BLINK)
		#On laisse l'utilisateur entrée son choix qui sera mit en majuscule automatiquement				
		choix = win2.getkey().upper()
		i = 2
		#Saisie controlée des choix disponibles
		while choix != 'N' and choix != 'L' and choix != 'S' and choix != 'C' and choix != 'Q':
			win2.addstr(int(maxY/8)+10, int(maxX/2)+13+i, " ", curses.A_BLINK)
			#On laisse l'utilisateur faire un autres choix
			choix= win2.getkey().upper()
			i+=1
		#On rafraichit la page pour tout afficher
		win2.refresh()
		#Puis on efface tout
		win2.clear()
		#Et on ferme la fenetre
		curses.endwin()
	#On retourne le choix de l'utilisateur
	return choix


#####################################################################


