import math

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    # Function to check if a player has won
    for i in range(3):
        # Check rows and columns for a win
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Function to check if the board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def evaluate(board):
    # Function to evaluate the current state of the board
    if is_winner(board, Computer):
        # If the computer wins, return a positive score
        return 1
    elif is_winner(board, Choice):
        # If the player wins, return a negative score
        return -1
    elif is_board_full(board):
        # If it's a tie, return 0
        return 0
    else:
        # If the game is ongoing, return None
        return None

def minimax(board, depth, is_maximizing, alpha, beta):
    # Minimax algorithm with alpha-beta pruning
    score = evaluate(board)

    if score is not None:
        # If the game is over, return the score
        return score

    if is_maximizing:
        max_eval = -math.inf
        # Maximizing player (computer) tries to maximize the score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Try placing Computer in an empty cell
                    board[i][j] = Computer
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    # Undo the move
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        # Prune the remaining possibilities if necessary
                        break
        return max_eval
    else:
        min_eval = math.inf
        # Minimizing player (player) tries to minimize the score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Try placing Choice in an empty cell
                    board[i][j] = Choice
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    # Undo the move
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        # Prune the remaining possibilities if necessary
                        break
        return min_eval

def find_best_move(board):
    # Function to find the best move for the computer player
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Try placing Computer in an empty cell
                board[i][j] = Computer
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                # Undo the move
                board[i][j] = ' '

                if move_val > best_val:
                    # Update the best move if a better move is found
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    # Function to play the Tic-Tac-Toe game
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's turn
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if col>2 or row>2:
            print("Out of Range. Try again.")
            continue
        elif board[row][col] == ' ':
            # Place Choice in the selected cell
            board[row][col] = Choice
        else:
            print("Cell already occupied. Try again.")
            continue

        if is_winner(board, Choice):
            # Check if the player has won
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            # Check if the board is full (tie)
            print_board(board)
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn:")
        best_move = find_best_move(board)
        # Place 'X' in the best move cell
        board[best_move[0]][best_move[1]] = Computer

        if is_winner(board, Computer):
            # Check if the computer has won
            print_board(board)
            print("Sorry, you lose. Better luck next time!")
            break

        if is_board_full(board):
            # Check if the board is full (tie)
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    Choice = input("Choose X or O: ")
    if Choice == "X" or Choice == "x":
        Computer = "O"
        play_game()
    elif Choice == "O" or Choice == "o":
        Computer = "X"
        play_game()
    else:
        print("Wrong input.")
    
