
#from Modules import Choose_Player_Marker

#
#from Modules import Choose_First
#from Modules import Check_Free_Space

#from Modules import Player_Choice


#*********************************************************
#           This function place a marker on board
#*********************************************************
def place_marker(board,marker,position):
  

    board[position] = marker
    

    return(board)