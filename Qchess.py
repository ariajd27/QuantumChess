import quantum_chess as ch

#Quantum chess simulator using my chess library.

game = ch.QuantumChessGame()
#ch.verbose = 3

def plural_s(quantity):
	if quantity == 1:
		return ''
	else:
		return 's'

while True:
	number_of_universes = len(game.instances)
	print(f'{number_of_universes} universe{plural_s(number_of_universes)} currently in superposition.')

	ch.visualize_superposition(game)

	move = input('Input a move:') #ex. d2d4 for normal moves, q d2 for quantum moves.

	if move == 'exit':
		break

	elif move[0] == 'q': #Placing a piece in a superposition between all its possible moves.
		try:
			start_square = move[-2:]
			game.superposition(from_square=start_square)
		except Exception as e:
			print(str(e) + ' Please try again.')
			continue

	elif len(move) == 4: #Normal move.
		try:
			game.move(move)
		except Exception as e:
			print(str(e) + ' Please try again.')
			continue

	else:
		print('Unknown move.\nex: \'d2d4\' for normal moves, \'q d2\' for quantum moves.')

