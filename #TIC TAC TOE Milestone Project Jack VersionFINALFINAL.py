#TIC TAC TOE Milestone Project Jack Version

#FUNCTION TO ASSIGN A PLAYER MARKER GLOBALLY 

import random


def player_assignment():
	global player1
	global player2
	
	player1=''

	while player1 not in ['X','O']:

	    player1=input('Hello Player 1, are you gonna be X or O?')
	
	if player1 == 'X':


	    player2 = 'O'

	else:

		player2 = 'X'
	

#FUNCTION TO DISPLAY THE GAME BOARD
def display_board(board):
	print('    '+board[7]+'    '+'|'+'    '+board[8]+'    '+'|'+'    '+board[9]+'    ')
	print('-----------------------')
	print('    '+board[4]+'    '+'|'+'    '+board[5]+'    '+'|'+'    '+board[6]+'    ')
	print('-----------------------')
	print('    '+board[1]+'    '+'|'+'    '+board[2]+'    '+'|'+'    '+board[3]+'    ')


#FUNCTION TO RETURN PLAYER POSITION CHOICE 
def player_choice():

	position = 0

	while position not in range(1,10):

		position = int(input('Choose a Position 1-9'))
	
	return int(position)
	

#THIS IS THE FUNCTION THAT WILL PLACE PLAYER'S CHOICE AT POSITION
def place_marker(board,player,position):
	board[position]=player
	

#FUNCTION TO CHECK WHOSE TURN IT IS 
def turn():
	number = random.randint(0,1)
	
	if number == 0:
		return 'Player 1'
	
	else:
		return 'Player 2'
	
	
#THIS WILL CHECK IF THERES A WIN ACROsS ROWS AND COLUMNS AS A BOOLEAN
def win_check(board,marker):
	
	return ((board[1] == board[2] == board[3] == marker) or
(board[4] == board[5] == board[6] == marker) or 
(board[7] == board[8] == board[9] == marker) or
(board[7] == board[4] == board[1] == marker) or
(board[8] == board[5] == board[2] == marker) or
(board[9] == board[6] == board[3] == marker) or
(board[1] == board[5] == board[9] == marker) or 
(board[3] == board[5] == board[7] == marker) )

#THIS WILL CHECK IF THE BOARD IS FULL TO DETERMINE IF ITS A TIE OR NOT
def full_board_check(board):
	return '' not in board
	





	#LETS START THE GAME


	#FIRST THINGS FIRST
print('Welcome to TIC TAC TOE')

game_on = True

game_board = ['','','','','','','','','','']

turn = turn()

player_assignment()


while game_on == True:




		#WE START BY DISPLAYING THE BOARD

		#NOW WE ASSIGN THE PLAYER 



		#NOW PLAYER1 AND PLAYER2 WILL HAVE GLOBAL ASSIGNMENTS
		#NOW WE WILL DO A FLIP AND SEE WHO STARTS THE GAME


	if turn == 'Player 1':

		print('\n'*100)
		print('Its Player 1 Turn')


		display_board(game_board)
		position = player_choice() 
		place_marker(game_board,player1,position)


		if win_check(game_board,player1) == True:
			
			display_board(game_board)
			print('\n'*100)
			print('Player 1 Has Won!')
			game_on == False

		else:

			if full_board_check(game_board) == True:
				
				display_board(game_board)
				print('\n'*100)
				print('Its a TIE!')

			else:
				turn = 'Player 2'

	else:

		print('\n'*100)
		print('Its Player 2 Turn')

		display_board(game_board)
		position = player_choice() 
		place_marker(game_board,player2,position)

		if win_check(game_board,player2) == True:
			
			display_board(game_board)
			print('\n'*100)
			print('Player 2 Has Won!')
			game_on == False

		else:

			if full_board_check(game_board) == True:
				
				display_board(game_board)
				print('\n'*100)
				print('Its a TIE!')

			else:
				turn = 'Player 1'













	
