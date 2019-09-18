#*********************************************************
#           This function checks free space on the board
#*********************************************************
  
def full_board_check(board):
   
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True
    else:
        return False
   

