from Modules import Check_Free_Space
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
