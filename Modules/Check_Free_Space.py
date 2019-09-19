from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker
from Modules import Win_Check
from Modules import Choose_First
from Modules import Check_Free_Space
from Modules import Full_Board_Check
from Modules import Player_Choice
from Modules import Replay

#*******************************************************************
#           This function checks particular position is free or not
#*******************************************************************
def space_check(board,position):
    

        if board[position] == ' ':
            return True
        else:
            return False

