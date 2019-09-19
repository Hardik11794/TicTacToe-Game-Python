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
#           This function ask player for replay
#********************************************************************************

def replay():

        ask_replay = input("Do you want to play again ? ").upper()
        if ask_replay == "YES":
            return True
        else:
            return False
    
