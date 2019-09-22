from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker
from Modules import Win_Check
from Modules import Choose_First
from Modules import Check_Free_Space
from Modules import Full_Board_Check
from Modules import Player_Choice
from Modules import Replay
#*********************************************************
#           This function checks free space on the board
#*********************************************************
  
def full_board_check(board):
   
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' \
        and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True
    else:
        return False
   

