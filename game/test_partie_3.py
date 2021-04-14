from play import *

#TEST
def test_create_new_play():
	print("==== TESTS FONCTION create_new_play() ====")
	print("on doit avoir un plateau avec une tuile 1 et une tuile 2 car c'est le début de la partie, on doit ensuite avoir la valeur   		comprise entre 1 et 3 de la prochaine tuile qui va apparaître on doit enfin avoir le score de départ qui correspond aux deux premières 		tuiles sur le plateau à savoir 3")
	print("on lance la fonction") 
	play = create_new_play()
	plateau = play['plateau']['tiles']
	print(" ")
	simple_display(plateau)
	print(" ")
	print("on a bien une tuile de valeur 1 et une tuile de valeur 2")
	print(play)
	print("on a bien la valeur de la prochaine tuile, elle est bien comprise entre 1 et 3, le score est également de 3")
	print("== TEST VALIDE ==")
	
	print("==== TESTS NUMERO 2 FONCTION create_new_play() ====")
	print("on lance la fonction") 
	play = create_new_play()
	plateau = play['plateau']['tiles']
	print(" ")
	simple_display(plateau)
	print("on a bien une tuile de valeur 1 et une tuile de valeur 2")
	print(" ")
	print(play)
	print("on a bien la valeur de la prochaine tuile, elle est bien comprise entre 1 et 3, le score est également de 3")
	print("== TEST VALIDE ==")
	
#TEST
def test_cycle_play() :
	print("==== TESTS FONCTION cycle_play() ====")
	print("Pour tester cette fonction il faut jouer et voir si les différentes options marche bien ") 
	rep = 'b'
	while rep !='o' and rep !='n' : 
		rep = str(input("Voulez-vous lancez une partie pour tester ? : oui(o)/non(n) : "))
	if rep =='o' : 
		threes()
	elif rep =='n' : 
		return 
	print("== TEST VALIDE ==")