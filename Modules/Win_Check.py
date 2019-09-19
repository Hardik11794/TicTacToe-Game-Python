from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker
from Modules import Win_Check
from Modules import Choose_First
from Modules import Check_Free_Space
from Modules import Full_Board_Check
from Modules import Player_Choice
from Modules import Replay
#import TicTacToe



#*********************************************************
#           This function checks win
#*********************************************************

def win_check(board,marker):
   
    if board[1]==board[5]==board[9]== marker or board[3]==board[5]==board[7]== marker or board[1]==board[2]==board[3]== marker or board[4]==board[5]==board[6]== marker or board[7]==board[8]==board[9]== marker or board[7]==board[4]==board[1]== marker or board[8]==board[5]==board[2]== marker or board[9]==board[6]==board[3]== marker:
        
        return True
    else:
        return False

