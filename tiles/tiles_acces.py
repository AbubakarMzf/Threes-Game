# coding: utf-8

import sys
from os import path
sys.path.append('../')
from ui.play_display import *


######################### FONCTION PARTIE 1 #########################


#Verifie que l'indice donner correspond a un indice valide par rapport a n
def check_indice(plateau, indice):
	 if int(indice) < plateau["n"] and int(indice) >= 0:
	 	return True
	 return False


#On vérifie si les coordonnees en parametres corresponde a une case existante
def check_room(plateau, lig, col):
	#Si les 2 coordonnees sont valides on return True sinon False
	if check_indice(plateau, lig) and check_indice(plateau, col):
		return True
	return False


#On retourne la valeur correspondant a la case donnée
def get_value(plateau, lig, col):
	#On verifie que les coordonnees sont valides
	assert check_room(plateau, lig, col), "Case non valide"
	#Une ligne est compose de 4 valeurs 
	#les coordonees peuvent etres = 0
	#4*lig = 1ere colonne de la ligne lig
	return plateau["tiles"][4*lig + col]


#On donne une valeur a une case du plateau
def set_value(plateau, lig, col, val):
    #On verifie que les coordonnees sont valides et que la valeur est positive ou = 0
    #On génere une erreur avec une absurdité quand la case est non valide
    assert check_room(plateau, lig, col) or val >= 0, "Case non valide"
    if get_value(plateau,lig,col) == 0 : 
    #on regarde si on va mettre la valeur dans une case libre
    #Comme une nouvelles cases est prises on enleves 1 au nombres de cases libres
        plateau["nombres_cases_libres"] = plateau["nombres_cases_libres"] - 1        
    #On met la valeur
    plateau["tiles"][4*lig + col] = val


#On vérifie si la case de coordonnees i, j est vide
def is_room_empty(plateau, i, j):
	#On génere une erreur quand la case est non valide
	assert check_room(plateau, i, j), "Case non valide"
	#Si case vide on return True sinon on return False
	if plateau["tiles"][4*i + j] == 0:
		return True
	return False


#####################################################################
