import random


def display_board(square):
    row1_4_7_9 = ['     |     |     ']
    row3_6 = ['_____|_____|_____']
    row2 = ['  ' + square[7] + '  |  ' + square[8] + '  |  ' + square[9]]
    row5 = ['  ' + square[4] + '  |  ' + square[5] + '  |  ' + square[6]]
    row8 = ['  ' + square[1] + '  |  ' + square[2] + '  |  ' + square[3]]

    print('\n' * 100)
    print(''.join(row1_4_7_9))
    print(''.join(row2))
    print(''.join(row3_6))
    print(''.join(row1_4_7_9))
    print(''.join(row5))
    print(''.join(row3_6))
    print(''.join(row1_4_7_9))
    print(''.join(row8))
    print(''.join(row1_4_7_9))


def player_input():
    marker = ''
    acceptable_p1_choice = ['X', 'O']

    while marker not in acceptable_p1_choice:
        marker = input('P1 would you like to be X or O?').upper()

    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def marker_placement(board, marker, position):
    board[position] = marker


def winner(square, mark):
    # 789
    # 456
    # 123
    return ((square[7] == mark and square[5] == mark and square[3] == mark) or  # diagonal1
            (square[9] == mark and square[5] == mark and square[1] == mark) or  # diagonal2
            (square[7] == mark and square[4] == mark and square[1] == mark) or  # vertical1
            (square[8] == mark and square[5] == mark and square[2] == mark) or  # vertical2
            (square[9] == mark and square[6] == mark and square[3] == mark) or  # vertical3
            (square[7] == mark and square[8] == mark and square[9] == mark) or  # horizontal1
            (square[4] == mark and square[5] == mark and square[6] == mark) or  # horizontal2
            (square[1] == mark and square[2] == mark and square[3] == mark))  # horizontal3


def first_turn():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def square_available(board, position):
    return board[position] == ' '  # if position on board is empty, return True for square available


def board_full(board):
    for i in range(1, 10):  # check squares 1-9
        if square_available(board, i) == True:  # if any squres 1-9 are available (TRUE), then board is not full
            return False
    return True


def player_choice(board):
    position = 0  # set position to a number not in 1-9

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not square_available(board, position):
        position = int(input('Choose your next position: (1-9)'))

    return position


def play_again():
    return (input('Do you want to play again? Yes or No:').upper().startswith('Y'))


print('Let\'s play Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = first_turn()
    print(turn + ' will go first.')

    play_game = input('Ready to play? Yes or No:')

    if play_game.upper() == 'Y':
        continue_game = True
    else:
        continue_game = False

    while continue_game:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            marker_placement(theBoard, player1_marker, position)

            if winner(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has won!')
                continue_game = False
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            marker_placement(theBoard, player2_marker, position)

            if winner(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                continue_game = False
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break
