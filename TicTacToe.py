
import random

print("This is TicTacToe  !!!")
print(' ')


#*********************************************************
#           This function print a board
#*********************************************************
def display_board(board):
    print(board[7],'|',board[8],'|',board[9])
    print(board[4],'|',board[5],'|',board[6])
    print(board[1],'|',board[2],'|',board[3])




#*********************************************************
#           This function choose player and marker
#*********************************************************

def player_input():
    
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input("Player 1 Choose your marker 'X' or 'O' : ").upper()

    player1 = marker

    if player1 == 'X':
          player2 = 'O'
    else:
        player2 = 'X'
    print(" ")
    print(f"Player 1 is {player1}.")
    print(f"Player 2 is {player2}.")
    return player1,player2
    


#*********************************************************
#           This function place a marker on board
#*********************************************************
def place_marker(board,marker,position):
  

    board[position] = marker
    

    return(board)

#*********************************************************
#           This function checks win
#*********************************************************

def win_check(board,marker):

    if board[1]==board[5]==board[9]== marker or board[3]==board[5]==board[7]== marker or board[1]==board[2]==board[3]== marker or board[4]==board[5]==board[6]== marker or board[7]==board[8]==board[9]== marker or board[7]==board[4]==board[1]== marker or board[8]==board[5]==board[2]== marker or board[9]==board[6]==board[3]== marker:
        display_board(print_board)
       
        return True
    else:
        return False

#*********************************************************
#           This function decides who will go first
#*********************************************************
       
def choose_first(player1,player2):
    random_player = random.randint(0,1)
    if random_player == 0:
        print(f"Player 1 will go first with marker {player1}")
        player1Turn = True
        player2Turn = False
        
    elif random_player == 1:
        print(f"Player 2 will go first with marker {player2}")
        player1Turn = False
        player2Turn = True
        
    return player1Turn,player2Turn

   
#*******************************************************************
#           This function checks particular position is free or not
#*******************************************************************
  
def space_check(board,position):
    

        if board[position] == ' ':
            return True
        else:
            return False

#*********************************************************
#           This function checks free space on the board
#*********************************************************
  
def full_board_check(board):
   
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True
    else:
        return False
   

       
#********************************************************************************
#           This function ask player for position and checks if it is available
#********************************************************************************


def player_choice(board):

    while True:
        position = int(input("Enter your next position(1-9) : ")) 
        if space_check(board,position) == True:
            return int(position)
            break
        else:
            print('This position has been filled up, Choose another one.')
            continue
    
 

#********************************************************************************
#           This function ask player for replay
#********************************************************************************

def replay():

        ask_replay = input("Do you want to play again ? ").upper()
        if ask_replay == "YES":
            return True
        else:
            return False
    




while True:
    print_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1,player2 = player_input()                                             #This function choose player and marker.
    print(" ")
    player1Turn,player2Turn = choose_first(player1,player2)                      #This function decides who will go first.
    
    while True:  
        if player1Turn == True and player2Turn == False: 
            
            
            display_board(print_board)                                           #This function display the board
            print(" ")
            print('Player 1,Your turn !!')
            print(" ")
            position = player_choice(print_board)                                #This function ask player for position and checks if it is available
            place_marker(print_board,player1,position)                           #This function place a marker on board
            if win_check(print_board,player1) == True:                           #This function checks for win
                print('Congtulations, Player 1 won !!')
                break
            if full_board_check(print_board) == False:                         #This function checks if board is full or not
                player1Turn = False
                player2Turn = True
           
            if full_board_check(print_board) == True:
              display_board(print_board)
              print("Game is Draw !!")
              break
      
        else: 
         player1Turn == False and player2Turn == True
        
         display_board(print_board)                                           #This function display the board
         print(" ")
         print('Player 2,Your turn !!')
         print(" ")
         position = player_choice(print_board)                                #This function ask player for position and checks if it is available
         place_marker(print_board,player2,position)                           #This function place a marker on board
        
         
         if win_check(print_board,player2) == True:                           #This function checks for win
              print('Congtulations, Player 2 won !!')
              break
         
         if full_board_check(print_board) == False:                         #This function checks if board is full or not
              player1Turn = True 
              player2Turn = False

         if full_board_check(print_board) == True:
              display_board(print_board)
              print("Game is Draw !!")
              break
        
          
    if replay() == False:                                                     #This function ask player for display
        break
               
         






