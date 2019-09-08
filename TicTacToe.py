
import random

print("This is TicTacToe")
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
    
    for space in board:
        if space == ' ':
            return False
        else:
            return True
        break

       
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

        ask_replay = input("Do you want to play again ? ")
        if ask_replay == "Yes":
            return True
        else:
            return False
    



#while True:
print_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

player1,player2 = player_input()                                         #This function choose player and marker.
print(" ")
player1Turn,player2Turn = choose_first(player1,player2)    #This function decides who will go first.
    
while True:  
        
    if player1Turn == True and player2Turn == False: 
            print(" ")
            print('Player 1,Your turn !!')
            print(" ")
            display_board(print_board)
            position = player_choice(print_board)                                #This function ask player for position and checks if it is available
            place_marker(print_board,player1,position)                           #This function place a marker on board
            
            if win_check(print_board,player1) == True:
                
                print('Congtulations, Player 1 won !!')
                break
            elif full_board_check(print_board) == False:
                player1Turn = False
                player2Turn = True
                
            else:
                print("Game is Draw !!")
                break
                

           

    else: 
         player1Turn == False and player2Turn == True
         print(" ")
         print('Player 2,Your turn !!')
         print(" ")
         display_board(print_board)
         position = player_choice(print_board)                                #This function ask player for position and checks if it is available
         place_marker(print_board,player2,position)                           #This function place a marker on board
         
         if win_check(print_board,player2) == True:
                
                print('Congtulations, Player 2 won !!')
                break
         elif full_board_check(print_board) == False:
              player1Turn = True 
              player2Turn = False
              
         else:
              print("Game is Draw !!")
              break
          
               
         






