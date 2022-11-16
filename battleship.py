MY_SHIPS = [[''] * 8 for x in range(8)]
MY_GUESS = [[''] * 8 for x in range(8)]

convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


from random import randint


def print_game(game): 
    print('    A B C D E F G H')
    print('    ---------------')
    row_count = 1
    for row in game:
        print("%d|%s|" % (row_count, "|".join(row)))
        row_count += 1


def guess_ship():
    pass


def make_ships():
    pass


def ship_hits():
    pass


make_ships()
goes = 10
while goes > 0:
