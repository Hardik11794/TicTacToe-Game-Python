
print("This is TicTacToe")
print(' ')

print_board = ['#','O','X','0','X','O','X','O','X','O']

def display_board(board):
    print(board[7],'|',board[8],'|',board[9])
    print(board[4],'|',board[5],'|',board[6])
    print(board[1],'|',board[2],'|',board[3])


display_board(print_board)

print(' ')

player_num = int(input("Select player number 1 or 2: "))
player_sign = input('Choose X or O sign: ')

if player_num == '1'and player_sign == 'X':
    First_player = player_num
    First_Sign = 'X'
    Second_player = ''
    Second_Sign = 'O'

