import random
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

