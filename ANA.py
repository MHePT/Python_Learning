import math

def Display(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="") 
		for col in range(3):
                  if str(board[row][col]) != "X" and  str(board[row][col]) != "O":
                       print("|   " + str((3 * row + col + 1)) + "   ", end="")
                  else:
                       print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def Winner_is(board,sgn):
    
	if sgn == Computer:	
		who = "Computer"
	elif sgn == Player:
		who = "Player"
	else:
		who = None
	cross1 = cross2 = True 
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
			return who
		if board[rc][rc] != sgn:
			cross1 = False
		if board[2 - rc][2 - rc] != sgn:
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def Tie_Or_Not(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def Score(board):

    if Winner_is(board, Computer) == "Computer":

        return 1
    elif Winner_is(board, Player) == "Player":

        return -1
    elif Tie_Or_Not(board):

        return 0
    else:

        return None

def minimax(board, is_maximizing, alpha, beta):
    score = Score(board)

    if score is not None:
        return score

    if is_maximizing:
        alpha = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = Computer
                    eval = minimax(board, False, alpha, beta)
                    # Undo the move
                    board[i][j] = ' '
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return alpha
    else:
        beta = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = Player
                    eval = minimax(board, True, alpha, beta)
                    # Undo the move
                    board[i][j] = ' '
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return beta

def Highest_Score(board):
    highest_val = -math.inf
    Which_Move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = Computer
                this_score = minimax(board, False, -math.inf, math.inf)
                board[i][j] = ' '

                if this_score > highest_val:
                    Which_Move = (i, j)
                    highest_val = this_score

    return Which_Move

def enter_move(board):
	ok = False	
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("Bad move - repeat your input!")
			continue
		move = int(move) - 1 	
		row = move // 3 	
		col = move % 3		
		sign = board[row][col]	
		ok = sign not in ['O','X'] 
		if not ok:	
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = Player 	

    # Main Code
Player = input("Choose X or O: ").upper()
if Player == "X":
    Computer = "O"
elif Player == "O":
    Computer = "X"
else:
    print("Wrong input.")
    Start= False;

Start = True
board = [[' ' for _ in range(3)] for _ in range(3)]

while Start:
    
    Display(board)
    
    enter_move(board)  

    if Winner_is(board, Player) == "Player":
            
     Display(board)
     print("You wins!")
     break

    if Tie_Or_Not(board):
        Display(board)
        print("It's a tie!")
        break

    print("Computer's turn:")
    best_move = Highest_Score(board)
    board[best_move[0]][best_move[1]] = Computer

    if Winner_is(board, Computer) == "Computer":

        Display(board)
        print("Computer wins!")
        break

    if Tie_Or_Not(board):

        Display(board)
        print("It's a tie!")
        break
    
