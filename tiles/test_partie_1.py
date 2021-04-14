# coding: utf-8

from tiles_moves import *
from tiles_acces import *


######################### FONCTION TEST tiles_move #########################


def test_get_nb_empty_rooms():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	p["nombres_cases_libres"] = 3
	print("On teste la fonction get_nb_empty_rooms() sur ", p, "avec un faux nombres de cases libres : 3")
	n = get_nb_empty_rooms(p)
	print("La fonction corrige le nombres de cases libres de", p, "avec", n, "cases libres")
	print("== TEST VALIDE ==")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [0, 2, 0, 0, 0, 3, 1, 2, 0, 6, 0, 2, 0, 6, 1, 2]}
	p["nombres_cases_libres"] = 2
	print("On teste la fonction get_nb_empty_rooms() sur ", p, "avec un faux nombres de cases libres : 2")
	n = get_nb_empty_rooms(p)
	print("La fonction corrige le nombres de cases libres de", p, "avec", n, "cases libres")
	print("== TEST VALIDE ==")
	print(" ")


#####################################################################


######################### FONCTION TEST tiles_acces #########################


def test_check_indice():
	p = init_play()
	print("==== TESTS FONCTION check_indice() ====")
	print("On teste la fonction sur ", p)
	print("Si indice = 0 on doit trouver True")
	print("On trouve : ", check_indice(p, 0))
	print("Si indice = 10 on doit trouver False")
	print("On trouve : ",check_indice(p, 10))
	print("Si indice = 2 on doit trouver True")
	print("On trouve : ", check_indice(p, 0))
	print("Si indice = -1 on doit trouver False")
	print("On trouve : ",check_indice(p, 10))
	print("== TEST VALIDE ==")
	print(" ")
	

def test_check_room():
	p = init_play()
	print("==== TESTS FONCTION check_room() ====")
	print("On teste la fonction sur ", p)
	print("Si lig = 2 et col = 1 on doit trouver True")
	print("On trouve : ", check_room(p, 2,1))
	print("Si lig = 10 et col = 2 on doit trouver False")
	print("On trouve : ", check_room(p, 10,2))
	print("Si lig = -1 et col = 3 on doit trouver False")
	print("On trouve : ", check_room(p, -1,3))
	print("Si lig = 3 et col = 3 on doit trouver True")
	print("On trouve : ", check_room(p, 3,3))
	print("== TEST VALIDE ==")
	print(" ")

def test_get_value():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	print("==== TESTS FONCTION get_value() ====")
	print("On teste la fonction sur :")
	simple_display(p)
	print("Si lig = 0 et col = 0 on doit trouver la valeur 6")
	print("On trouve : ", get_value(p, 0,0))
	print("Si lig = 2 et col = 3 on doit trouver la valeur 2")
	print("On trouve : ", get_value(p, 2,3))
	rint("Si lig = 1 et col = 3 on doit trouver la valeur 2")
	print("On trouve : ", get_value(p, 1,3))
	print("Si lig = 2 et col = 3 on doit trouver la valeur 0")
	print("On trouve : ", get_value(p, 3,0))
	print("== TEST VALIDE ==")
	print(" ")

def test_set_value():
	p = init_play()
	print("==== TESTS FONCTION set_value() ====")
	print("On teste la fonction sur :")
	simple_display(p)
	print("On ajoute 3 cases : -1ere , lig = 0 col = 0 val = 1")
	print("-2eme, lig = 1 col = 2 val = 3")
	print("-3eme, lig = 2 col = 3 val = 6")
	set_value(p, 0,0,1)
	set_value(p, 1,2,3)
	set_value(p, 2,3,6)
	print("On trouve :")
	simple_display(p)
	print("== TEST VALIDE ==")
	print(" ")

def test_is_room_empty():
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	assert is_room_empty(p, 0,1) == False
	assert is_room_empty(p, 0,3) == True
	assert is_room_empty(p, 2,1) == False
	assert is_room_empty(p, 3,0) == True
	print("==== TESTS FONCTION is_room_empty() ====")
	print("On teste la fonction sur :")
	simple_display(p)
	print("Pour lig = 0 et col = 1 case remplie donc on doit trouver False")
	print("On trouve : ", is_room_empty(p, 0, 1))
	print("Pour lig = 2 et col = 1 case remplie donc on doit trouver False")
	print("On trouve : ", is_room_empty(p, 2, 1))
	print("Pour lig = 0 et col = 3 case vide donc on doit trouver True")
	print("On trouve : ", is_room_empty(p, 0, 3))
	print("Pour lig = 3 et col = 0 case vide donc on doit trouver True")
	print("On trouve : ", is_room_empty(p, 3, 0))
	print("== TEST VALIDE ==")
	print(" ")
	

#####################################################################