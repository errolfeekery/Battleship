from random import randint


MY_SHIPS = [[''] * 8 for x in range(8)]
MY_GUESS = [[''] * 8 for x in range(8)]

convert = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def print_game(game):
    print('    A B C D E F G H')
    print('    ---------------')
    row_count = 1
    for row in game:
        print("%d|%s|" % (row_count, "|".join(row)))
        row_count += 1


def make_ships(game):
    for boat in range(5):
        boat_row, boat_column = randint(0, 7), randint(0, 7)
        while game[boat_row][boat_column] == 'X':
            boat_row, boat_column = randint(0, 7), randint(0, 7)
        game[boat_row][boat_column] = 'X'


def guess_ship():
    row = input('Place ship row 1-8')
    while row not in '12345678':
        pint('Enter a valid row')
        row = input('Place ship row 1-8')
    column = input('Place ship in column A-H').lower()
    while column not in 'ABCDEFGH':
        print('Enter a valid column')
        column = input('Place ship in column A-H').lower()
        return int(row) - 1, convert[column]


def ship_hits(game):
    counter = 0
    for row in game:
        for column in row:
            if column == 'X':
                counter += 1
        return counter


make_ships(MY_SHIPS)
goes = 10
print_game(MY_SHIPS)
print_game(MY_GUESS)
# while goes > 0:
