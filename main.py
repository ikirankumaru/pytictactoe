import random


def display_board(board):
    '''
    OUTPUT: Show the tictactoe board
    '''
    print('\n' * 100)
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

def win_check(board, mark):
    '''OUTPUT: Returns True for Win'''
    return (
        (board[1] == board[2] == board[3] == mark) or 
        (board[4] == board[5] == board[6] == mark) or 
        (board[7] == board[8] == board[9] == mark) or 
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or 
        (board[3] == board[6] == board[9] == mark) or 
        (board[3] == board[5] == board[7] == mark) or
        (board[1] == board[5] == board[9] == mark)
    )

def choose_first():
    '''
    OUTPUT: Randonly decide which player goes first
            Return a string of which player went first
            Player 1 / Player 2
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    
    return 'Player 1'

def space_check(board, position):
    '''OUTPUT: Returns a boolean indicating whether a space on the board is freely available'''

    return board[position] == ' '

def full_board_check(board):
    '''OUTPUT: True if full, False otherwise.'''

    for i in range(1,10):
        if space_check(board, i):
            return False
        
    return True

def player_choice(board):
    '''OUTPUT: Choose the next position, returns the position if its available'''

    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = input('Choose your next position: (1-9) ')
        
        if position.isdigit():
            position = int(position)
    
    return position

def replay():
    '''OUTPUT: Return True if they do want to play again.'''

    return input('Do you want to play again (y/n) ? ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    game_on = False
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play game? (y/n) ')

    if play_game.lower()[0] == 'y':
        game_on = True
        
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player1 has won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player2 has won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
