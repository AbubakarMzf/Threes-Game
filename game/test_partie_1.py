from play import *

#TEST
def test_is_game_over():
	print("==== TESTS FONCTION is_game_over() ====")
	print("on commence avec le plateau suivant : ")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	assert is_game_over(p) == False
	print("== TEST VALIDE ==")
	print("Des cases sont vides donc des mouvements sont encore possible donc le jeu n'est pas fini")
	print("==== TESTS NUMERO 2 FONCTION is_game_over() ====")
	print("on prend le plateau suivant")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 12, 1, 3, 1, 2, 2, 6, 3, 2, 3, 6, 1, 2]}
	assert is_game_over(p) == True
	print("== TEST VALIDE ==")
	print("aucune case n'est libre ET AUCUN mouvement n'est possible")
	print("==== TESTS NUMERO 3 FONCTION is_game_over() ====")
	print("on prend le plateau suivant")
	p = {"n" : 4, "nombres_cases_libres" : 0, "tiles" : [1, 2, 1, 2, 1, 3, 1, 2, 2, 6, 3, 2, 3, 6, 1, 2]}
	assert is_game_over(p) == False
	print("== TEST VALIDE ==")
	print("aucune case n'est libre MAIS MOUVEMENT POSSIBLE SUR LA PREMIERE LIGNE")
	

#TEST
def test_init_play():
	print("==== TESTS FONCTION init_play() ====")
	print("vérifions si la fonction init_play() nous donne bien un plateau conforme")
	assert init_play() == {'n': 4, 'nombres_cases_libres': 16, 'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
	print("== TEST VALIDE ==")
	print("==== TESTS NUMERO 2 FONCTION init_play() ====")
	print("vérifions si la fonction init_play() nous donne bien un plateau conforme")
	assert init_play() == {'n': 4, 'nombres_cases_libres': 16, 'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
	print("== TEST VALIDE ==")

#TEST
def test_get_score():
	print("==== TESTS FONCTION get_score() ====")
	p = {"n" : 4, "nombres_cases_libres" : 4, "tiles" : [6, 2, 1, 0, 0, 3, 1, 2, 0, 6, 3, 2, 0, 6, 1, 2]}
	assert get_score(p) == 35
	print("== TEST VALIDE ==")
	print("==== TESTS NUMERO 2 FONCTION get_score() ====")
	p = {"n" : 4, "nombres_cases_libres" : 0, "tiles" : [6, 2, 1, 12, 1, 3, 1, 2, 2, 6, 3, 2, 3, 6, 1, 2]}
	assert get_score(p) == 53
	print("== TEST VALIDE ==")