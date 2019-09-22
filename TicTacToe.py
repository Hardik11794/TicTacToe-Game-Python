
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


def runPlayer(print_board, player):
    position = Player_Choice.player_choice(print_board)                               #This function ask player for position and checks if it is available
    Place_Marker.place_marker(print_board, player, position)                           #This function place a marker on board

    if Win_Check.win_check(print_board, player) == True:                              #This function checks for win
        Display_Board.display_board(print_board)
        print('Congtulations, ' + player + ' won !!')
        return False

    if Full_Board_Check.full_board_check(print_board) == True:
        Display_Board.display_board(print_board)
        print("Game is Draw !!")
        return False

while True:

    print_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1, player2 = Choose_Player_Marker.player_input()                                     #This function choose player and marker.
    print(" ")
    playerFlip = True
    
    while True:  

        Display_Board.display_board(print_board)                                          #This function display the board
        if playerFlip == True: 
            print( "\n PLayer 1 Your turn !! \n")
            if(runPlayer(print_board, player1) == False):
                break
        else:
            print( "\n PLayer 2 Your turn !! \n")
            if(runPlayer(print_board, player2) == False):
                break
        playerFlip = not(playerFlip)
        
    if Replay.replay() == False:                                                             #This function ask player for display
        break
               
         






