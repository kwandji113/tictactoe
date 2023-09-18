# use a 3-d array to represent the game board 
#zero feature relase 
# Print out in ASCII first before focusing on GUI first
#For simplicity, in my implementation of minimax, since x is always the player, they will be the maximizer, and o, the ai, will be the minimizer
#For easy mode, will just select a random cell from open cells, or willpick less optimal path from minimax
import math
import random


#Intizalizing the game board
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
#declaring player and ai variables
player , ai = 'x','o'


# Functions to make sure that there are moves left on the board


def moves_left(board):
     for i in range(3):
        for j in range(3):
            if(board[i][j] == "_"):
                 return True
    
     return False



#evaluate: A function that evaluates the current state of the game and returns a vlaue based on wether there is a win, loss or tie for the current player 
def evalute(board):
    #checking the rows to see if anyone has has won
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][2] and board[row][0] != "_"):
            if board[row][0] == 'X':  #X is the player 
               return 10  
            else: 
                return -10
    
    #checking the columns to see if anyone has one 
    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] and board [0][col] != "_"):
            if board[0][col] == 'X':
                return 10
            else:
                return -10
    
    if(board[0][0] == board[1][1] == board [2][2] and board[0][0] != "_"):
            if board[0][0] == 'X':  #X is the player 
               return 10  
            else: 
                return -10     
    
    if(board[0][2] == board[1][1] == board[2][0] and board[1][1] != "_"):
        if board[row][0] == 'X':  #X is the player 
               return 10  
        else: 
                return -10
                  
    return 0
        
    
    
    

def minimax(board, size: int, isMaximizer: bool):
     #when usig minimax, I have to evlauvte one of three base cases:
     # 1.) User, or x, has won
     # 2.) AI, or O, has won
     # 3.) Tie/board is full
     
     value = evalute(board)
     if(value == 10):
          return value
     
     if(value == -10):
          return value

     if(moves_left(board) == False):
        return 0
    
#check whos turn it is inside of the recusion

     if(isMaximizer == True):
        score = -1000

    # Find all possible moves for the AI to make
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = player
                    score = max(score,minimax(board, size + 1, False))
                    board[i][j] = '_'
        return score



     else:
        score = 1000
        
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = ai
                    score = min(score,minimax(board,size + 1,True))
                    board[i][j] = '_'
        
        return score

def move(board):
    val = -100
    move = (0,0)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == "_"):
                board[i][j] = ai
                new_val = minimax(board,0,False)
                board[i][j] = "_"
            
                if(new_val > val):
                    val = new_val
                    move = (i,j)

    return move            

def play_game(): 
    print("Welcome to Tic-Tac-Toe!")
    for x in board:
        print(" | ".join(x))
        print("-" * 9)
    game_mode = input(f"Single or mutliplayer? S for single, M for multiplayer:")

    if game_mode.lower() == "s":
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if(board[row][col] != "_"):
                print("Not a valid move. Try again")
                continue
            else:
                board[row][col] = player
                _print(board)
                check = evalute(board)
                
                if check == -10:
                    print("You have won!")
                    break
                if check == 10:
                    print(" Sorry, you lost!")
                    break
                if moves_left(board) != True:
                    print("It's a tie")
                    break
                else:
                    ai_move = move(board)
                    board[ai_move[0]][ai_move[1]] = ai
                    print("AI has moved \n")
                    _print(board)
                    loop = evalute(board)
                    if loop == -10:
                        print("You have won!")
                        break
                    if loop == 10:
                        print(" Sorry, you lost!")
                        break
                    if moves_left(board) != True:
                        print("It's a tie")
                        break
    
    if game_mode.lower() == "m":
        current_player = 'x'
        while(True):
            print(f"Player {current_player}'s turn")
            row = int(input("Enter row (0, 1, or 2): " ))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] != "_":
                print("That spot is already taken. Try again.")
                continue
            else:
                board[row][col] == current_player
            
            _print(board)
            
            if check_win(board,current_player):
                print(f"Player {current_player} wins!")
                break
            elif moves_left(board) != True:
                print("It's a tie!")
                break
            
            current_player = 'x' if current_player == 'o' else 'o'

                        
def check_win(board,player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def _print(board):
    for x in board:
        print(*x, sep = "  | ") 


play_game()