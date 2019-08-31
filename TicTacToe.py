
print("This is TicTacToe")
print(' ')

#print_board = ['#','O','X','0','X','O','X','O','X','O']
print_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#*********************************************************
#           This function print a board
#*********************************************************
def display_board(board):
    print(board[7],'|',board[8],'|',board[9])
    print(board[4],'|',board[5],'|',board[6])
    print(board[1],'|',board[2],'|',board[3])


display_board(print_board)
print( ' ')

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
    return(player1,player2)

player_input()
#*********************************************************
#           This function place a marker on board
#*********************************************************
def place_marker(board,marker,position):

    board.insert(position,marker)
    display_board(board)

    return(board)

#*********************************************************
#           This function checks win
#*********************************************************

def win_check(board,marker):

    if board[1]==board[5]==board[9]== marker or board[3]==board[5]==board[7]== marker or board[1]==board[2]==board[3]== marker or board[4]==board[5]==board[6]== marker or board[7]==board[8]==board[9]== marker or board[7]==board[4]==board[1]== marker or board[8]==board[5]==board[2]== marker or board[9]==board[6]==board[3]== marker:
        print(f'{marker} You Win,Congratulations !!!')
        return True
    else:
        return False


place_marker(print_board,'X',1)
win_check(print_board,'X')
place_marker(print_board,'X',5)
win_check(print_board,'X')
place_marker(print_board,'X',9)
win_check(print_board,'X')
