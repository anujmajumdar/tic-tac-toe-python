# Global Variables

board = [" ", " ", " ",
 				 " ", " ", " ", 
 				 " ", " ", " "]

current_player = 'X'

winner = ""

game_status = "ongoing"

#instructions
def instructions():
	global current_player
	print("Welcome to 2 Player tic-tac-toe! positions on the board are shown below:")
	print("1" + " | " + "2" + " | " + "3")
	print("--|---|--" )
	print("4" + " | " + "5" + " | " + "6")
	print("--|---|--" )
	print("7" + " | " + "8" + " | " + "9")
	current_player = input("Who wants to start first? X or O : ")
	current_player = current_player.upper()
	print("Let's Go!")

#display

def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print("--|---|--" )
	print(board[3] + " | " + board[4] + " | " + board[5])
	print("--|---|--" )
	print(board[6] + " | " + board[7] + " | " + board[8])

#flip player

def flip_player():
	global current_player

	if current_player == 'X':
		current_player = 'O'
	else:
		current_player = 'X'

#handle turn

def handle_turn():
	global current_player
	position = int(input("Choose a position from 1-9 on the board to place: ")) - 1
	if board[position] == " ":
		board[position] = current_player
		flip_player()
		display_board()
	else:
		print("That spot is already taken! Try again: ")

#check row

def check_rows():
	global winner, game_status
	if board[0] == board[1] and board[1] == board[2] and board[1]!=" ":
		winner = board[1]
		game_status = "ended"
	elif board[3] == board[4] and board[4] == board[5] and board[4]!=" ":
		winner = board[4]
		game_status = "ended"
	elif board[6] == board[7] and board[7] == board[8] and board[7]!=" ":
		winner = board[7]
		game_status = "ended"

#check column

def check_columns():
	global winner, game_status
	if board[0] == board[3] and board[3] == board[6] and board[3]!=" ":
		winner = board[3]
		game_status = "ended"
	elif board[1] == board[4] and board[4] == board[7] and board[4]!=" ":
		winner = board[4]
		game_status = "ended"
	elif board[2] == board[5] and board[8] == board[8] and board[5]!=" ":
		winner = board[5]
		game_status = "ended"

#check diagonal

def check_diagonals():
	global winner, game_status
	if board[0] == board[4] and board[4] == board[8] and board[4]!=" ":
		winner = board[4]
		game_status = "ended"
	elif board[2] == board[4] and board[4] == board[6] and board[4]!=" ":
		winner = board[4]
		game_status = "ended"

#check tie

def check_tie():
	global game_status, winner
	if board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
		game_status = "ended"
		winner = "none"

#check win

def check_win():
	check_rows()
	check_columns()
	check_diagonals()

#play game

def play_game():
	global winner, game_status
	while game_status!="ended":
		handle_turn()
		check_win()
		check_tie()
	
instructions()
play_game()
if winner!="none":
	print(f"The winner is {winner}!")
else:
	print("It's a tie!")
