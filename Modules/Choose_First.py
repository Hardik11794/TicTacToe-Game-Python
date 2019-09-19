import random
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

