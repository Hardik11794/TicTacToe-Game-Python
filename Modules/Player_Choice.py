from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker
from Modules import Win_Check
from Modules import Choose_First
from Modules import Check_Free_Space
from Modules import Full_Board_Check
from Modules import Player_Choice
from Modules import Replay

#********************************************************************************
#           This function ask player for position and checks if it is available
#********************************************************************************


def player_choice(board):

    while True:
        position = int(input("Enter your next position(1-9) : ")) 
        if Check_Free_Space.space_check(board,position) == True:
            return int(position)
            break
        else:
            print('This position has been filled up, Choose another one.')
            continue
