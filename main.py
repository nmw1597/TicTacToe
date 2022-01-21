#This is a TicTacToe game

# To Do:
#############################
# 1. Create game board
# 2. Player choose X or O
# 3. Player choose square on game board
# 4. Check if player won
# 5. Ask if play again


#Create Game board
def game_board():
    print('\n'*100)
    print("Each number represents the square\n     |     |\n  7  |  8  |  9\n_____|_____|_____\n     |     |\n  4  |  5  |  6\n_____|_____|_____\n     |     |\n  1  |  2  |  3\n     |     |     \n\n")

    square = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    row1_4_7_9 = ['     |     |     ']
    row3_6 = ['_____|_____|_____']
    row2 = ['  ' + square[6] + '  |  ' + square[7] + '  |  ' + square[8]]
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


def choose_xo():
    p1 = ''
    p1_choice = False
    acceptable_p1_choice = ['x', 'o', 'X', 'O']

    while p1_choice == False:

        p1 = input("Player 1, would you like to be X or O?")

        if p1 not in acceptable_p1_choice:
            print("Please select X or O")
        else:
            p1 = p1.capitalize()
            print(f'You have chosen {p1}')
            p1_choice = True

    return p1.capitalize()


def choose_square():

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

    return int(square_choice)



game_board()
choose_xo()
choose_square()