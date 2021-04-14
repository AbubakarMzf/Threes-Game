from play import *

#TEST
def test_save_game_and_restrore_game() : 
	print("==== TESTS FONCTION save_game() & restore_game() ====")
	print("Pour tester cette fonction vous pouvez commencer une partie puis mettre menu et la sauvegarder")
	print("Une fois cela fait vous commencer une  nouvelle partie puis vous chargez l'ancienne")
	print("Si vous retouvez bien votre partie le test est validé")
	rep = 'b'
	while rep !='o' and rep!='n' : 
		rep = str(input("Voulez-vous lancez une partie pour tester ? : oui(o)/non(n) : "))
	if rep =='o' : 
		threes()
	elif rep =='n' : 
		return 