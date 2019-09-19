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
