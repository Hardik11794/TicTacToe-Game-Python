

#*********************************************************
#           This function choose player and marker
#*********************************************************

def player_input():
    
    marker = ''

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
    return player1, player2
