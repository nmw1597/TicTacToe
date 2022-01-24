#This is a TicTacToe game

# To Do:
#############################
# 1. Create game board
# 2. Player choose X or O
# 3. Player choose square on game board
# 4. Check if player won
# 5. Ask if play again


#Create Game board
def gameboard():
    print('\n'*100)
    print("Each number represents the square\n     |     |\n  7  |  8  |  9\n_____|_____|_____\n     |     |\n  4  |  5  |  6\n_____|_____|_____\n     |     |\n  1  |  2  |  3\n     |     |     \n\n")

    square = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    row1_4_7_9 = ['     |     |     ']
    row3_6 = ['_____|_____|_____']
    row2 = ['  ' + square[8] + '  |  ' + square[7] + '  |  ' + square[6]]
    row5 = ['  ' + square[5] + '  |  ' + square[4] + '  |  ' + square[3]]
    row8 = ['  ' + square[2] + '  |  ' + square[1] + '  |  ' + square[0]]

    print("Current Game Board")
    print(''.join(row1_4_7_9))
    print(''.join(row2))
    print(''.join(row3_6))
    print(''.join(row1_4_7_9))
    print(''.join(row5))
    print(''.join(row3_6))
    print(''.join(row1_4_7_9))
    print(''.join(row8))
    print(''.join(row1_4_7_9))


#allows player1 to choose if they want to be X or O
def marker():
    p1_xo = ''
    p1_choice = False
    acceptable_p1_choice = ['x', 'o', 'X', 'O']

    while p1_choice == False:

        p1_xo = input("Player 1, would you like to be X or O?")

        if p1_xo not in acceptable_p1_choice:
            print("Please select X or O")
        else:
            p1_xo = p1_xo.capitalize()
            print(f'Player 1 has chosen {p1_xo}')
            p1_choice = True

    if p1_xo == 'X'
        turn = ['X','O','X','O','X','O','X','O','X']
    else
        turn = ['O','X','O','X','O','X','O','X','O']

    return turn


def position():

    square_range = range(1, 10)
    square_is_digit = False
    square_in_range = False

    while square_is_digit == False or square_in_range == False:

        square_choice = input("Pick a square. (1-9)")

        # check if digit
        if square_choice.isdigit() == False:
            print("Your choice is not a digit.")
        else:
            square_is_digit = True

        # check if within range
        if square_choice.isdigit():
            if int(square_choice) not in square_range:
                print("Your choice is not within range. Please choose a number between 1-9")
            else:
                square_in_range = True

    return (int(square_choice) - 1)           #return the square number as int.  subtract 1 so it matches the square numbers

def winner():

    win = [[6,5,2], [7,4,1], [8,3,0], [6,7,8], [5,4,3], [2,1,0], [6,4,3], [8,4,2]]
    square_check_p1 = []
    square_check_p2 = []
    p1_wins = False
    p2_wins = False

    if square_check_p1 in win:
        print('Player 1 WINS!')
        p1_wins = True
    elif square_check_p2 in win:
        print('Player 2 WINS!')
        p2_wins = True
    else:
        pass

    return p1_wins
    return p2_wins

def place_selection(gameboard, marker, position):

    gameboard = ['','','','','','','','','']

    position = position()

    if gameboard == ['','','','','','','','','']:
        position = position()
        turn = marker()
        marker = turn[0]
    marker = marker()

    gameboard[position] = marker

    return(gameboard)

def game():

    gameboard()
    xo =

place_selection(gameboard, marker, position)