#*******************************************************************
#           This function checks particular position is free or not
#*******************************************************************
def space_check(board,position):
    

        if board[position] == ' ':
            return True
        else:
            return False

