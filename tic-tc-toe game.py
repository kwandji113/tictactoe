# use a 3-d array to represent the game board 
#zero feature relase 
# Print out in ASCII first before focusing on GUI first

#For simplicity, in my implementation of minimax, since x is always the player, they will be the maximizer, and o, the ai, will be the minimizer




#Intizalizing the game board
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]


#evaluate: A function that evaluates the current state of the game and returns a vlaue based on wether there is a win, loss or tie for the current player 
def evalute(board):
    #checking the rows to see if anyone has has won
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][3]):
            if board[row][0] == 'X':  #X is the player 
               return 10  
            else: 
                return -10
    
    #checking the columns to see if anyone has one 
    for col in range(3):
        if(board[0][col] == board[1]col == board[2][col]):
            if board[0][col] == 'X':
                return 10
            else:
                return -10
    
    if(board[0][0] == board[1][1] == board [2][2]):
            if board[0][0] == 'X':  #X is the player 
               return 10  
            else: 
                return -10     
    
    if(board[0][2] == board[1][1] == board[2][0]):
        if board[row][0] == 'X':  #X is the player 
               return 10  
        else: 
                return -10
                  
    return 0
        
    
            
        
