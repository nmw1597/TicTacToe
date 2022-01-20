#This is a TicTacToe game

# To Do:
#############################
# 1. Create game board
# 2. Player choose X or O
# 3. Player choose square on game baord
# 4. Check if player won
# 5. Ask if play again


#Create Game board
def game_board():

    # 1'         |         |         '
    # 2'   {7}   |   {8}   |   {9}   '
    # 3'_________|_________|_________'
    # 4'         |         |         '
    # 5'   {4}   |   {5}   |   {6}   '
    # 6'_________|_________|_________'
    # 7'         |         |         '
    # 8'   {1}   |   {2}   |   {3}   '
    # 9'         |         |         '

    # row1_4_7 = ['         |         |         ']
    # row3_6 = ['_________|_________|_________']
    # row9 = ['         |         |         ']
    # row2 = ['   {7}   |   {8}   |   {9}   ']
    # row5 = ['   {4}   |   {5}   |   {6}   ']
    # row8 = ['   {1}   |   {2}   |   {3}   ']
    row1_4_7 = ['     |     |     ']
    row3_6 = ['_____|_____|_____']
    row9 = ['     |     |     ']
    row2 = [' ',7,' | ',8,' | ',9,' ']
    row5 = [' {4} | {5} | {6} ']
    row8 = [' {1} | {2} | {3} ']

    print(row1_4_7)
    print(row2)
    print(row3_6)
    print(row1_4_7)
    print(row5)
    print(row3_6)
    print(row1_4_7)
    print(row8)
    print(row9)

    print(type(row2))

game_board()