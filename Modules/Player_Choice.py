from Modules import Display_Board
from Modules import Choose_Player_Marker
from Modules import Place_Marker

from Modules import Check_Free_Space


#********************************************************************************
#           This function ask player for position and checks if it is available
#********************************************************************************


def player_choice(board):

    while True:
       try:
             while True:
                position = int(input("Enter your next position(1-9) : ")) 
                if position >=1 and position <=10:
                    break
                else:
                    print("\nValue must be between 1 - 9 \n")
           
       except:
           print("\nEnter only integer 1- 9 number \n")
       else:
              
              
              if Check_Free_Space.space_check(board,position) == True:
                  return int(position)
                  break
              else:
                  print('This position has been filled up, Choose another one.')
                  continue
