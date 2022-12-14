from random import randint


HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                      'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    row = input('Enter a ship row 1-8 /n')
    while row not in '12345678':
        print('Enter a valid row')
        row = input('Enter a ship row 1-8 /n')
    column = input('Enter a ship column A-H /n').upper()
    while column not in 'ABCDEFGH':
        print('Enter a valid column')
        column = input('Please enter a ship column A-H /n').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hits_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
        return count


create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('Already selected')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Direct hit!')
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("Miss!")
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hits_ships(GUESS_BOARD) == 5:
        print('You sunk my battleships!')
        break
    print('You have ' + str(turns) + ' goes left')
    if turns == 0:
        print('Game is over!')
        break
