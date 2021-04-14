# coding: utf-8

from colorama import *

init()


######################### FONCTION PARTIE 1 #########################


def simple_display(plateau):
	lig = ""
	i = 0
	while i < len(plateau["tiles"]):
		lig = lig + str(plateau["tiles"][i]) + " "
		if (i+1)%4 == 0:
			print(lig)
			lig = ""
		i += 1
		
def full_display(plateau):

	"""
		Affichage du plateau en couleurs avec le bibliothéque colorama
	"""
	
	#On prend seulement le plateau de jeu
	plato = plateau['tiles']
	#Tailles des cases
	espace = "         "
	#On initialise les lignes
	ligne = ""
	ligne2 = ""
	i = 0
	while i < len(plato):
		#On parcours le plateau et a chaque valeurs on attribut la couleur qui lui corresponds
		#On utilise colorama
		val = plato[i]
		if val == 1:
			#Les espaces détermine la taille de la case
			#Une ligne contient les valeurs avec le nombres d'espaces qu'il faut autour
			ligne += "    " + Back.BLUE + ("    " + str(val) + "    ") + Style.RESET_ALL
			#Une autre ligne contient les espace qui seront colorés pour créée la case
			ligne2 += "    " + Back.BLUE + (espace) + Style.RESET_ALL
			#On additionne ces cases séparés par des espaces
		elif val == 2:
			ligne += "    " + Back.RED + str("    " + str(val) + "    ") + Style.RESET_ALL
			ligne2 += "    " + Back.RED + (espace) + Style.RESET_ALL
		elif val == 0: 
			ligne += "    " + Back.BLUE + str(espace) + Style.RESET_ALL 
			ligne2 += "    " + Back.BLUE + str(espace) + Style.RESET_ALL
		elif len(str(val))>1:
			ligne += "    " + Fore.BLACK + Back.WHITE + str("   " + str(val) + "    ") + Style.RESET_ALL 
			ligne2 += "    " + Back.WHITE + (espace) + Style.RESET_ALL
		else:
			ligne += "    " + Fore.BLACK + Back.WHITE + str("    " + str(val) + "    ") + Style.RESET_ALL 
			ligne2 += "    " + Back.WHITE + (espace) + Style.RESET_ALL
		#A chaque ligne complete créer c'est a dire contenant 4 cases on les print
		if (i+1)%4 == 0:
			print(espace)
			print(ligne2)
			print(ligne2)
			print(ligne)
			print(ligne2)
			print(ligne2)
			print(espace)
			#Et on remet les valeurs des lignes a vide
			ligne = ""
			ligne2 = ""
		i += 1


#####################################################################



		
		
