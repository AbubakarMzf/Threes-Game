# coding: utf-8

import sys
from os import path
sys.path.append('../') 
#sys.path.append('../tiles/')
from tiles.tiles_acces import *
#sys.path.append('../ui/')
from ui.play_display import *
from random import *

######################### FONCTION PARTIE 1 #########################


def get_nb_empty_rooms(plateau):

	"""
		Met a jour le dicionnaire plateau avec le nombre de case libre(s) du plateau et renvoie le nombre de case(s) libre(s)
	"""
	nb_empty_rooms = 0
	i = 0
	#On parcourt les cases
	while i < len(plateau["tiles"]):
		#Si case vide on ajoute 1 au compteur de case vide
		if plateau["tiles"][i] == 0:
			nb_empty_rooms += 1
		i += 1
	#On modifie la valeur dans le dictionnaire
	plateau["nombres_cases_libres"] = nb_empty_rooms
	return nb_empty_rooms


#####################################################################


######################### FONCTION PARTIE 2 #########################


#On trouve un dictionnaire contenant les informations des/de la tuile(s) générer aléatoirement en fonction du mode
def get_next_alea_tiles(plateau, mode):

	"""
		Retourne une ou deux tuiles dont la position (lig,col) est tirée aléatoirement et correspond à un emplacement du plateau.
	    plateau : dictionnaire contenant la plateau du jeu 
	    mode : 'init' : un dictionnaire contenant deux tuiles de valeur 1 et 2 est retourné. La position de chaque tuile est tirée aléatoirement et correspond à un emplacement libre du plateau ; ce mode est utilisé lors de l'initialisation du jeu.
		ou mode : 'encours' : un dictionnaire contenant une tuile, de valeur comprise entre 1 et 3 est retournée. La position de la tuile est tirée aléatoirement et correspond à un emplacement libre du plateau ; ce mode est utilisé en cours de jeu  
	"""

	next_tiles = {}
	next_tiles["mode"] = mode
	#Si on est en mode Initialisation on a 2 tuiles
	if mode == "init":
		#Génération des 2 tuiles aléatoirement (toutes les cases sont vides)
		coord_t1 = {"val" : 1, "lig" : randint(0,3), "col" : randint(0,3)}
		coord_t2 = {"val" : 2, "lig" : randint(0,3), "col" : randint(0,3)}
		#On vérifie que les tuiles ne sont pas sur la meme case 
		while coord_t2["lig"] == coord_t1["lig"] and coord_t2["col"] == coord_t1["col"]:
			coord_t2 = {"val" : 2, "lig" : randint(0,3), "col" : randint(0,3)}
		next_tiles['0'] = coord_t1
		next_tiles['1'] = coord_t2
	#Si on est en mode encours on a 1 tuiles 
	elif mode == "encours":
		#Génération des coordonnés aléatoirement
		lig = randint(0,3)
		col = randint(0,3)
		#On vérifie que la case est vide sinon on recherche d'autres coordonnées d'une case vide
		while not is_room_empty(plateau, lig, col):
			lig = randint(0,3)
			col = randint(0,3)
		coord_t1 = {"val" : randint(1,3), "lig" : lig, "col" : col} 
		next_tiles['0'] = coord_t1
	#On definit la clef check en fonction de si le jeux est fini ou non
	next_tiles["check"] = True
	return next_tiles

def put_next_tiles(plateau, tiles):

	""" 
		Permet de placer une ou deux tuiles dans le plateau. 
		plateau : plateau de jeu 
		tiles : dictionnaire sous la forme de celui renvoyé par la fonction get_next_alea_tiles
	"""

	i = 0
	#len(tiles)-2 = nb de tuiles
	while i < len(tiles)-2:
		set_value(plateau, tiles[str(i)]["lig"], tiles[str(i)]["col"], tiles[str(i)]["val"])
		i += 1


def line_pack(plateau,num_lig,debut,sens) :

	"""
		Tasse les tuiles d'une ligne dans un sens donné. plateau : dictionnaire contenant le plateau du jeu 
	   	num_lig : indice de la ligne à tasser 
	   	debut : indice à partir duquel se fait le tassement 
	   	sens : du tassement, 1 vers la gauche et 0 vers la droite
	"""

	#On determine l'indice de la tuile du debut du tassement
	indice = 4*num_lig + debut 
    #Sens vers la gauche
	if sens == 1:
    	#On affecte la valeur 0 à la tuile du debut du tassement
		plateau['tiles'][indice] = 0
		#on va déplacer cette tuile jusqu'à la positionner à la fin de la ligne c'est-à-dire jusqu'à ce que son indice de positionnement+1 soit
		#divisible par 4      
		while (indice+1)%4 != 0 :
			a = plateau['tiles'][indice]#on stock la tuile du debut du tassement dans a 
			b = plateau['tiles'][indice+1] #on stock la tuile qui est juste après dans b 
		    #on switch la position des deux tuiles
			plateau['tiles'][indice] = b  
			plateau['tiles'][indice+1] = a
			indice+=1    #nouvelle position de la tuile du début du tassement
    #sens vers la droite 
	elif sens == 0 :
	#On affecte la valeur 0 à la tuile du debut du tassement
		plateau['tiles'][indice] = 0  
		#on va déplacer cette tuile jusqu'à la positionner au debut de la ligne
		while indice%4 !=0 :
			a = plateau['tiles'][indice]  #on stock la tuile du debut du tassement dans a 
			b = plateau['tiles'][indice-1]  #on stock la tuile qui est juste avant dans b
	        #on switch la position des deux tuiles 
			plateau['tiles'][indice] = b  
			plateau['tiles'][indice-1] = a
			indice-=1  #nouvelle position de la tuile du début du tassement



def colum_pack(plateau, num_col, debut, sens):

	"""
		Tasse les tuiles d'une colonne donnée dans un sens donné 
	   	plateau : dictionnaire contenant le plateau du jeu 
	   	debut : indice à partit duquel se fait le tassement
	   	numcol : indice de la colonne à tasser 
	   	sens : sens du tassement, 1 vers le haut et 0 vers le bas 
	"""

    #le parametre debut correspond a la ligne où se trouve la tuile du début du tassement
	ligne = debut 
    #on determine la position de la tuile du début de tassement et on lui affcete la valeur 0 
	indice = 4*ligne+num_col
	plateau['tiles'][indice] = 0 
    #sens vers le haut 
	if sens == 1 : 
        #on va maitenant déplacer cette tuile jusqu'à ce qu'elle soit tout en bas de la colonne donc a la ligne 3
		while ligne !=3 :
			a = plateau['tiles'][indice]       #on stock la tuile du début de tassement dans a 
			b = plateau['tiles'][indice + 4]   #on stock la tuile d'après se trouvant dans la meme colonne dans b 
            #on switch leur position 
			plateau['tiles'][indice] = b
			plateau['tiles'][indice + 4 ] = a
			indice+=4 #la tuile de début de tassement se trouve à la ligne suivante mais toujours dans la meme colonne donc +4
			ligne+=1 #nouvelle position de la tuile : elle se trouve a la ligne d'apres  
    #sens vers le bas 
	elif sens == 0 :
         #on va maitenant déplacer cette tuile jusqu'à ce qu'elle soit tout en haut de la colonne donc a la ligne 0
		while ligne !=0 : 
			a = plateau['tiles'][indice]   #on stock la tuile du début de tassement dans a 
			b = plateau['tiles'][indice - 4]  #on stock la tuile d'avant se trouvant dans la meme colonne dans b
            #on switch leur position 
			plateau['tiles'][indice] = b
			plateau['tiles'][indice - 4 ] = a
			indice-=4 #la tuile de début de tassement se trouve à la ligne d'avant mais toujours dans la meme colonne donc -4
			ligne-=1 #nouvelle position de la tuile  : elle se trouve a la ligne d'avant 


def line_move(plateau,num_lig,sens) : 

	"""
		Déplacement des tuiles d'une ligne donnée dans un sens donné en appliquant les règles du jeu threes
	    plateau : dictionnaire contenant le plateau du jeu 
	    num_lig : indice de la ligne pour laquelle il faut déplacer les tuiles 
	    sens : sens du déplacement des tuiles, 1 vers la gauche et 0 vers la droite
	"""

	#Sens vers la gauche
	if sens == 1:
    	#Si la premiere case a gauche est vide on tasse directement a partir de cette case
		if plateau['tiles'][4*num_lig] == 0 : 
        	#On tasse a partir du debut de la ligne a gauche
			line_pack(plateau,num_lig,0,1)
        #Sinon
		else :
			i = 0
        	#On parcourt la ligne de gauche a droite
			while i < 3 : 
				t1 = plateau['tiles'][4*num_lig + i]
				t2 = plateau['tiles'][4*num_lig + (i+1)]
        		#On regarde si les cases adjacentes peuvents fusionner
				if (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2 ) or (t1 == 2 and t2 == 1 ) and t1 != 0 and t2!=0: 
        			#On les fusionne en les additionnant
					plateau['tiles'][4*num_lig+i] += plateau['tiles'][4*num_lig + (i+1)]
        			#Puis on tasse a partir de la cases d'aprés celle qui ces formés
					line_pack(plateau,num_lig,i+1,1)
        			#Puis on sort de la boucle
					i = 3
        		#Si la cases est vide et qu'aucun tassement na était fait alors on tasse a partir de cette case vide
				elif t1 == 0:
					line_pack(plateau,num_lig,i,1)
				i+=1
	#Sens vers la droite
	elif sens == 0 :
		#Si la premiere case a droite est vide on tasse directement a partir de cette case
		if plateau['tiles'][4*num_lig+3] == 0 : 
			#On tasse a partir du debut de la ligne a droite
			line_pack(plateau,num_lig,3,0)   
		#Sinon     
		else :
			i = 3 
			#On parcours la ligne de droite a gauche
			while i > 0 : 
				t1 = plateau['tiles'][4*num_lig + i]
				t2 = plateau['tiles'][4*num_lig + (i-1)]
				#On regarde si les cases adjacentes peuvents fusionner
				if  (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2 ) or (t1 == 2 and t2 == 1 ) : 
					#On les fusionne en les additionnant
					plateau['tiles'][4*num_lig+i] += plateau['tiles'][4*num_lig + (i-1)]
					#Puis on tasse a partir de la cases d'aprés celle qui ces formés
					line_pack(plateau,num_lig,i-1,0)
					#Puis on sort de la boucle
					i = -1
				#Si la cases est vide et qu'aucun tassement na était fait alors on tasse a partir de cette case vide
				elif t1 == 0:
					line_pack(plateau,num_lig,i,0)
				i-=1

def column_move(plateau, num_col, sens):

	"""
		Déplacement des tuiles d'une colonne donnée dans un sens donné en appliquant les règles du jeu threes
	 	plateau : dictionnaire contenant le plateau du jeu 
	   	num_col : indice de la colonne pour laquelle il faut déplacer les tuiles
	   	sens : sens du déplacement des tuiles, 1 vers le haut et 0 vers le bas
	"""

	#Sens vers le bas
	if sens == 0 : 
		#Si la premiere case du bas est vide alors on tasse la colonne a partir de cette case
	    if plateau['tiles'][12 + num_col] == 0 : 
	        colum_pack(plateau,num_col,3,0)
	    #Sinon
	    else : 
	        i = 3
	        #On parcours la ligne du bas vers le haut
	        while i > 0 : 
	        	t1 = plateau['tiles'][4*i + num_col]
	        	t2 = plateau['tiles'][4*(i-1) + num_col]
	        	#On regarde si les cases adjacentes peuvents fusionner
	        	if (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2 ) or (t1 == 2 and t2 == 1 ):
	        		#On les fusionne en les additionnant
	        		plateau['tiles'][4*i + num_col] += plateau['tiles'][4*(i-1) + num_col]
	        		#Puis on tasse a partir de la cases d'aprés celle qui ces formés
	        		colum_pack(plateau,num_col,i-1,0)
	        		#Puis on sort de la boucle
	        		i = -1
	        	#Si la cases est vide et qu'aucun tassement na était fait alors on tasse a partir de cette case vide
	        	elif t1 == 0:
	        		colum_pack(plateau,num_col,i,0)
	        		i = -1
	        	i-=1
	#Sens vers le haut
	elif sens == 1 : 
		#Si la premiere case du haut est vide alors on tasse la colonne a partir de cette case
	    if plateau['tiles'][num_col] == 0 : 
	        colum_pack(plateau,num_col,0,1)
	    #Sinon
	    else : 
	        i = 0
	        #On parcours la ligne de haut en bas
	        while i < 3 :  
	        	t1 = plateau['tiles'][4*i + num_col]
	        	t2 = plateau['tiles'][4*(i+1) + num_col]
	        	#On regarde si les cases adjacentes peuvents fusionner
	        	if (t1 % 3==0 and t1 == t2) or (t1 == 1 and t2 == 2 ) or (t1 == 2 and t2 == 1 ) :
	        		#On les fusionne en les additionnant
	        		plateau['tiles'][4*i + num_col] += plateau['tiles'][4*(i+1) + num_col]
	        		#Puis on tasse a partir de la cases d'aprés celle qui ces formés
	        		colum_pack(plateau,num_col,i+1,1)
	        		#Puis on sort de la boucle
	        		i = 100
	        	#Si la cases est vide et qu'aucun tassement na était fait alors on tasse a partir de cette case vide
	        	elif t1 == 0:
	        		colum_pack(plateau,num_col,i,1)
	        	i+=1

def lines_move(plateau, sens):

	"""
		Déplace les tuiles de toutes les lignes du plateau dans un sens donné en appliquant les règles du jeu THREES. 
		plateau : dictionnaire contenant le plateau du jeu 
		sens : sens du déplacement, 1 vers la gauche et 0 vers la droite
	"""

	num_lig = 0
	#On parcours toutes les lignes
	while num_lig < 4:
		#On utilise la fonction line_move pour bouger les lignes une par une
		line_move(plateau, num_lig, sens)
		num_lig += 1

def columns_move(plateau, sens):

	"""
		Déplace les tuiles de toutes les colonnes du plateau dans un sens donné en appliquant les règles du jeu THREES. 
		plateau : dictionnaire contenant le plateau du jeu 
		sens : sens du déplacement, 1 vers le haut et 0 vers le bas
	"""

	num_col = 0
	#On parcours toutes les colonnes
	while num_col < 4:
		#On utilise la fonction column_move pour bouger les colonnes une par une
		column_move(plateau, num_col, sens)
		num_col += 1

def play_move(plateau, sens):

	"""
		Déplace les tuiles du plateau dans un sens donné en appliquant les règles du jeu Threes 
	    plateau : plateau de jeu 
	    sens : sens de déplacement des tuiles
	"""

	#Sens vers le bas
	if sens == "b":
		#Donc on bouge les colonnes vers le bas
		columns_move(plateau, 0)
	#Sens vers le haut
	elif sens == "h":
		#Donc on bouge les colonnes vers le haut
		columns_move(plateau, 1)
	#Sens vers la droite 
	elif sens == "d":
		#Donc on bouge les lignes vers la droite
		lines_move(plateau, 0)
	#Sens vers la gauche 
	elif sens == "g":
		#Donc on bouge les lignes vers la gauche
		lines_move(plateau, 1)


#####################################################################
