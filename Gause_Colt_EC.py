print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         Tic-Tac-Toe v.1.0.0
            By: Colt Gause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Instructions:
    > PLayer one will go first, entering their desired position first in the row (vertical axis), then in the column(horizontal axis).
    > The positions are 1, 2, 3 for both rows and columns. Going left to right, and top to bottom, respectively.
    > Play will continue until either player has matched three in a row going horizontally, vertically, or diagonally.
    > If the board fills up and neither player will is declared the winner, the game is a draw.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

board = [['-','-','-'],['-','-','-'],['-','-','-']]

x_vic = '''
!!!!!!!!!!!!!!!!!!!!!
    Player x Wins!
!!!!!!!!!!!!!!!!!!!!!
'''
o_vic = '''
!!!!!!!!!!!!!!!!!!!!!
    Player o Wins!
!!!!!!!!!!!!!!!!!!!!!
'''
tie = '''
!!!!!!!!!!!!!!!!!!!!!
     It's a tie!
!!!!!!!!!!!!!!!!!!!!!
'''
seperator = '''
--------------------------
        '''
occupied = '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    The cell you selected is occupied
           Please input another
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
invalid_input = '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    The value you entered is outside the range
        Please enter a number between 1 & 3
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

turn = 0
x = 'x'
o = 'o'
selected_space = ' '
game_over = False
valid_response = False
cell_occupied = False

def board_state():
    for row in board:
        print(' '. join(map(str, row)))

def win_condition():
    if board[0][0] == x:
        if board[0][1] == x:
            if board[0][2] == x:
                return True
        elif board[1][0] == x:
            if board[2][0] == x:
                return True
        elif board[1][1] == x:
            if board[2][2] == x:
                return True
    elif board[0][1] == x:
        if board[1][1] == x:
            if board[2][1] == x:
                return True
    elif board[0][2] == x:
        if board[1][2] == x:
            if board[2][2] == x:
                return True
        elif board[1][1] == x:
            if board[2][0] == x:
                return True
    elif board[1][0] == x:
        if board[1][1] == x:
            if board[1][2] == x:
                return True
    elif board[2][0] == x:
        if board[2][1] == x:
            if board[2][2] == x:
                return True
    
    if board[0][0] == o:
        if board[0][1] == o:
            if board[0][2] == o:
                return True
        elif board[1][0] == o:
            if board[2][0] == o:
                return True
        elif board[1][1] == o:
            if board[2][2] == o:
                return True
    elif board[0][1] == o:
        if board[1][1] == o:
            if board[2][1] == o:
                return True
    elif board[0][2] == o:
        if board[1][2] == o:
            if board[2][2] == o:
                return True
        elif board[1][1] == o:
            if board[2][0] == o:
                return True
    elif board[1][0] == o:
        if board[1][1] == o:
            if board[1][2] == o:
                return True
    elif board[2][0] == o:
        if board[2][1] == o:
            if board[2][2] == o:
                return True

while turn < 9 and game_over != True:
    if turn % 2 == 0:
        print(seperator)
        if cell_occupied == True:
            print(occupied)
            cell_occupied = False
        print('Player x\'s turn')
        board_state()
        while valid_response == False:
            row1 = int(input('Enter Selected Row: '))
            column1 = int(input('Enter Selected Column: '))
            if row1 in range(1, 4) and column1 in range(1, 4):
                valid_response = True
            else:
                print(seperator)
                print(invalid_input)
                print('Player x\'s turn')
                board_state()
        valid_response = False
        selected_space = board[row1 - 1][column1 - 1]
        if selected_space == '-':
            board[row1 - 1][column1 - 1] = x
            turn += 1
            game_over = win_condition()
        else:
            cell_occupied = True
            selected_space = ' '
    else:
        print(seperator)
        if cell_occupied == True:
            print(occupied)
        print('Player o\'s turn')
        board_state()
        while valid_response == False:
            row2 = int(input('Enter Selected Row: '))
            column2 = int(input('Enter Selected Column: '))
            if row2 in range(1, 4) and column2 in range(1, 4):
                valid_response = True
            else:
                print(seperator)
                print(invalid_input)
                print('Player o\'s turn')
                board_state()
        valid_response = False
        selected_space = board[row2 - 1][column2 - 1]
        if selected_space == '-':
            board[row2 - 1][column2 - 1] = o
            turn += 1
            game_over = win_condition()
        else:
            cell_occupied = True
            selected_space = ' '

if game_over == True:
    if turn % 2 == 0:
        print(seperator)
        board_state()
        print(o_vic)
    else:
        print(seperator)
        board_state()
        print(x_vic)
elif game_over != True:
    print(seperator)
    board_state()
    print(tie)
elif turn == 9:
    print(seperator)
    board_state()
    print(x_vic)