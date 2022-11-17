from random import randint


HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


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
    row = input('Place ship row 1-8 ')
    while row not in '12345678':
        print('Enter a valid row')
        row = input('Place ship row 1-8')
    column = input('Place ship in column A-H').upper()
    while column not in 'ABCDEFGH':
        print('Enter a valid column')
        column = input('Place ship in column A-H').upper()
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
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)

""" while goes > 0:
    print('This is Battleship')
    print_game(GUESS_BOARD)
    row, column = get_boat_location()
    if GUESS_BOARD[row][column] == '-':
        print('Already selected')
    elif GUESS_BOARD[row][column] == 'X':
        print('Direct hit!')
        GUESS_BOARD[row][column] = "X"
        goes -= 1
    else:
        print("Miss!")
        GUESS_BOARD[row][column] = '-'
        goes -= 1
    if boat_hits(GUESS_BOARD) == 5:
        print('You sunk my battleships!')
        break
    print('You have ' + str(goes) + ' goes left')
    if goes == 0:
        print('Game is over!')
    break

"""
