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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

board = [['-','-','-'],['-','-','-'],['-','-','-']]

turn = 0
x = 'x'
o = 'o'
selected_space = ' '
game_over = False

def board_state():
    for row in board:
        print(' '. join(map(str, row)))

def win_condition():
    if board[0][0] == x:
        if board[0][1] == x:
            if board[0][2] == x:
                board_state()
                print('Player x wins!')
                return True
        elif board[1][0] == x:
            if board[2][0] == x:
                board_state()
                print('Player x wins!')
                return True
        elif board[1][1] == x:
            if board[2][2] == x:
                board_state()
                print('Player x wins!')
                return True
    elif board[0][1] == x:
        if board[1][1] == x:
            if board[2][1] == x:
                board_state()
                print('Player x wins!')
                return True
    elif board[0][2] == x:
        if board[1][2] == x:
            if board[2][2] == x:
                board_state()
                print('Player x wins!')
                return True
        elif board[1][1] == x:
            if board[2][0] == x:
                board_state()
                print('Player x wins!')
                return True
    elif board[1][0] == x:
        if board[1][1] == x:
            if board[1][2] == x:
                board_state()
                print('Player x wins!')
                return True
    elif board[2][0] == x:
        if board[2][1] == x:
            if board[2][2] == x:
                board_state()
                print('Player x wins!')
                return True
    
    if board[0][0] == o:
        if board[0][1] == o:
            if board[0][2] == o:
                board_state()
                print('Player o wins!')
                return True
        elif board[1][0] == o:
            if board[2][0] == o:
                board_state()
                print('Player o wins!')
                return True
        elif board[1][1] == o:
            if board[2][2] == o:
                board_state()
                print('Player o wins!')
                return True
    elif board[0][1] == o:
        if board[1][1] == o:
            if board[2][1] == o:
                board_state()
                print('Player o wins!')
                return True
    elif board[0][2] == o:
        if board[1][2] == o:
            if board[2][2] == o:
                board_state()
                print('Player o wins!')
                return True
        elif board[1][1] == o:
            if board[2][0] == o:
                board_state()
                print('Player o wins!')
                return True
    elif board[1][0] == o:
        if board[1][1] == o:
            if board[1][2] == o:
                board_state()
                print('Player o wins!')
                return True
    elif board[2][0] == o:
        if board[2][1] == o:
            if board[2][2] == o:
                board_state()
                print('Player o wins!')
                return True

while turn < 9 and game_over != True:
    if turn % 2 == 0:
        print('Player x\'s turn')
        board_state()
        row1 = int(input('Enter Selected Row: '))
        column1 = int(input('Enter Selected Column: '))
        selected_space = board[row1 - 1][column1 - 1]
        if selected_space == '-':
            board[row1 - 1][column1 - 1] = x
            turn += 1
            game_over = win_condition()
        else:
            print('Cell Occupied.')
            selected_space = ' '
    else:
        print('Player o\'s turn')
        board_state()
        row2 = int(input('Enter Selected Row: '))
        column2 = int(input('Enter Selected Column: '))
        selected_space = board[row2 - 1][column2 - 1]
        if selected_space == '-':
            board[row2 - 1][column2 - 1] = o
            turn += 1
            game_over = win_condition()
        else:
            print('Cell Occupied.')
            selected_space = ' '

game_over = win_condition()

if game_over != True:
    board_state()
    print('Tie')
else:
    board_state()
    print('Player x Wins!')