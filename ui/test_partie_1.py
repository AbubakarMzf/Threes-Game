from play_display import *

def test_full_display():
	print("==== TESTS FONCTION full_display() ====")
	p = {'n': 4, 'nombres_cases_libres': 10, 'tiles': [2, 0, 1, 0, 2, 3, 0, 24, 0, 48, 0, 0, 0, 0, 0, 0]}
	print("On donne le plateau : ", p)
	print("On l'affiche : ")
	full_display(p)
	print("== TEST VALIDE ==")
	print("==== TESTS NUMERO 2 FONCTION full_display() ====")
	p = {'n': 4, 'nombres_cases_libres': 6, 'tiles': [0, 0, 24, 48, 2, 3, 0, 24, 0, 48, 0, 2, 1, 3, 12, 0]}
	print("On donne le plateau : ", p)
	lettre = get_user_move()
	print("On l'affiche : ")
	full_display(p)
	print("== TEST VALIDE ==")
	print(" ")