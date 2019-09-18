
from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker
from Modules import Win_Check
from Modules import Choose_First
from Modules import Check_Free_Space
from Modules import Full_Board_Check
from Modules import Player_Choice
from Modules import Replay


print("This is TicTacToe  !!!")
print(' ')

while True:
    print_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1,player2 = Choose_Player_Marker.player_input()                                             #This function choose player and marker.
    print(" ")
    player1Turn,player2Turn = Choose_First.choose_first(player1,player2)                      #This function decides who will go first.
    
    while True:  
        if player1Turn == True and player2Turn == False: 
            
            
            Display_Board.display_board(print_board)                             #This function display the board
            print(" ")
            print('Player 1,Your turn !!')
            print(" ")
            position = Player_Choice.player_choice(print_board)                                #This function ask player for position and checks if it is available
            Place_Marker.place_marker(print_board,player1,position)                           #This function place a marker on board
            if Win_Check.win_check(print_board,player1) == True:                           #This function checks for win
                print('Congtulations, Player 1 won !!')
                break
            if Full_Board_Check.full_board_check(print_board) == False:                           #This function checks if board is full or not
                player1Turn = False
                player2Turn = True
           
            if Full_Board_Check.full_board_check(print_board) == True:
              Display_Board.display_board(print_board)
              print("Game is Draw !!")
              break
      
        else: 
         player1Turn == False and player2Turn == True
        
         Display_Board.display_board(print_board)                                           #This function display the board
         print(" ")
         print('Player 2,Your turn !!')
         print(" ")
         position = Player_Choice.player_choice(print_board)                                #This function ask player for position and checks if it is available
         Place_Marker.place_marker(print_board,player2,position)                           #This function place a marker on board
        
         
         if Win_Check.win_check(print_board,player2) == True:                           #This function checks for win
              print('Congtulations, Player 2 won !!')
              break
         
         if Full_Board_Check.full_board_check(print_board) == False:                         #This function checks if board is full or not
              player1Turn = True 
              player2Turn = False

         if Full_Board_Check.full_board_check(print_board) == True:
              Display_Board.display_board(print_board)
              print("Game is Draw !!")
              break
        
          
    if Replay.replay() == False:                                                     #This function ask player for display
        break
               
         






