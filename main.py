def display_board(board):
    '''
    OUTPUT: Show the tictactoe board
    '''
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    '''
    OUTPUT: (Player 1 Marker, Player 2 Marker)
    '''
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    
    return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# print(player_input())
# place_marker(test_board, '$', 8)
