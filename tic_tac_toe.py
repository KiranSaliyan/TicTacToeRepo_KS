# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)
import numpy as np 

# ... write as many functions as you need

def isfull(board):
    return all(cell != str(k) for k in range(10) for row in board for cell in row)

def print_board(board):
  for row in board:
    print(row)

def check_input(board, player):

   
    while True:
        inp = int(input(f"Turn for player {player} to enter number between 1 -9\n"))
        if inp == 100:
            return 0
        if inp > 9 or inp < 0 or inp == " ":
            print("Invalid entry. Retry")
            continue
        else:
            row,col = (inp - 1) // 3, (inp - 1) % 3
            type(board[row][col])
            if board[row][col] == str(inp):
              board[row][col] = player
              break
            else :
              print("Spot is taken. Retry")
              continue

    return board       
      
def checkwinner(board,player):
    
    for row in board:
        if all(cell == player for cell in row):
           
           return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
           return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
       
       return True

def updatewinner(board,player):
    
    for row in board:
        if all(cell == player for cell in row):
            board[row][0] = board[row][0] + '\u0336'
            board[row][1] = board[row][0] + '\u0336'
            board[row][2] = board[row][0] + '\u0336'
            return

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            board[0][col] = board[0][col] + '\u0336'
            board[1][col] = board[1][col] + '\u0336'
            board[2][col] = board[2][col] + '\u0336'
            return
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
       
       return True

def print_sampleboard(board):
    """Display the current game board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = [[str(r*3+c+1) for c in range(3)]  for r in range(3)]

    #newboard = [["/" for _ in range(3)] for _ in range(3)]
    #print_sampleboard(board)

    current_player = 'X'
    print_sampleboard(board)
    while True:
       
        board = check_input(board, current_player)
        res = checkwinner(board,current_player)
        if res == True:
            print(f"Player {current_player} is the winner")
            #board = updatewinner(board,current_player)
            print_sampleboard(board)
            break

        res = isfull(board)  
        if res == True:
            print("Match draw!! restart the match")
            board = [[str(r*3+c+1) for c in range(3)]  for r in range(3)]

        print_sampleboard(board)
        current_player = 'X' if current_player == 'O' else 'O'

    

