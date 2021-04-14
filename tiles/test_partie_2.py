# coding: utf-8

from tiles_moves import *
from tiles_acces import *


######################### FONCTION TEST tiles_move #########################


def test_get_next_alea_tiles():
	p = init_play()
	print("==== TESTS FONCTION get_next_alea_tiles() ====")
	print("On teste la fonction en mode init sur :")
	simple_display(p)
	print("On doit avoir un tableau de contenant les coordonées et la valeurs de 2 cases du plateau")
	print("On trouve", get_next_alea_tiles(p, "init"))
	print("== TEST VALIDE ==")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("On teste la fonction en mode encours sur :")
	simple_display(p)
	print("On doit avoir un tableau avec les coordonnées et la valeur d'une nouvelle tuile sur une case vide")
	print("On trouve", get_next_alea_tiles(p, "encours"))
	print("== TEST VALIDE ==")
	print(" ")

def test_put_next_tiles():
	p = init_play()
	print("==== TESTS FONCTION put_next_tiles() ====")
	print("On teste la fonction sur :")
	simple_display(p)
	put_next_tiles(p, get_next_alea_tiles(p, "init"))
	print("On doit trouver un plateau avec 2 nouvelles tuiles")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("On teste la fonction put_next_tiles() sur :")
	simple_display(p)
	put_next_tiles(p, get_next_alea_tiles(p, "encours"))
	print("On doit trouver un plateau avec 1 nouvelle tuile")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_line_pack():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION line_pack() ====")
	print("2 fois vers la gauche sur la deuxieme ligne du plateau :")
	simple_display(p)
	print("1ere fois début = 0")
	line_pack(p, 1, 0, 1)
	print("2eme fois début = 2")
	line_pack(p, 1, 2, 1)
	print("La ligne doit devenir 2,3,3,0 puis 2,3,0,0")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("Sur la meme ligne on teste le meme fonction vers la droite 2 fois")
	print("1ere fois début = 3")
	line_pack(p, 1, 3, 0)
	print("2eme fois début = 2")
	line_pack(p, 1, 2, 0)
	print("La ligne doit devenir 0,2,3,0 puis 0,0,2,0")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_colum_pack():
	p = {"n" : 4, "nombres_cases_libres" : 6, "tiles" : [1, 3, 0, 3, 6, 0, 12, 24, 3, 0, 2, 0, 1, 3, 0, 2]}
	print("==== TESTS FONCTION colum_pack() ====")
	print("3 fois vers le haut avec un début = 1 sur la deuxieme colonne du plateau :")
	simple_display(p)
	colum_pack(p, 1, 1, 1)
	colum_pack(p, 1, 1, 1)
	colum_pack(p, 1, 1, 1)
	print("La colonne doit devenir 3,0,3,0 puis 3,3,0,0 et 3,0,0,0")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("Sur la premiere colonne vers le bas 2 fois")
	colum_pack(p, 0, 3, 0)
	colum_pack(p, 0, 3, 0)
	print("La colonne doit devenir 0,1,6,3 puis 0,0,1,6")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_line_move():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION line_move() ====")
	print("2 fois vers la gauche sur la deuxieme ligne du plateau :")
	simple_display(p)
	line_move(p, 1, 1)
	print("La ligne doit devenir 2,3,3,0 puis 2,6,0,0")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("Sur la derniere ligne vers la droite 1 fois")
	line_move(p, 3, 0)
	print("La ligne doit devenir 0,0,6,3")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_column_move():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION column_move() ====")
	print("1 fois vers le haut sur le deuxieme colonne du plateau : ")
	simple_display(p)
	column_move(p, 1, 1)
	print("La colonne doit devenir 2,2,12,0")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("Sur la troisieme colonne vers le bas 1 fois")
	column_move(p, 2, 0)
	print("La colonne doit devenir 0,0,6,1")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_lines_move():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION lines_move() ====")
	print("2 fois vers la gauche sur le plateau :")
	simple_display(p)
	lines_move(p, 1)
	lines_move(p, 1)
	print("On doit trouver p = [2, 0, 0, 0, 2, 6, 0, 0, 6, 3, 2, 0, 6, 3, 0, 0]")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("1 fois sur le meme plateau vers la droite")
	lines_move(p, 0)
	print("On doit trouver p = [0, 0, 2, 0, 0, 0, 2, 6, 0, 6, 3, 2, 0, 0, 6, 3]")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_columns_move():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION columns_move() ====")
	print("2 fois vers le haut sur le plateau :")
	simple_display(p)
	columns_move(p, 1)
	columns_move(p, 1)
	print("On doit trouver p = [0, 2, 6, 3, 0, 2, 1, 2, 0, 12, 0, 2, 0, 0, 0, 0]")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print("1 fois sur le meme plateau vers le bas")
	columns_move(p, 0)
	print("On doit trouver p = [0, 0, 0, 0, 0, 2, 6, 3, 0, 2, 1, 2, 0, 12, 0, 2]")
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_play_move():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION play_move() ====")
	print("On test sur le plateau :")
	simple_display(p)
	print("Vers le bas (sens = b)")
	play_move(p, "b")
	simple_display(p)
	print("Vers le haut (sens = h)")
	play_move(p, "h")
	simple_display(p)
	print("Vers la droite (sens = d)")
	play_move(p, "d")
	simple_display(p)
	print("Vers la gauche (sens = g)")
	play_move(p, "g")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")


#####################################################################