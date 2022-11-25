#Legand
# @ for placing ship and hit battleship
# ' ' for available space
# 'M' for missed shot

from random import randint

hidden_board = [(' ') * 5 for x in range(5)]
guess_board = [(' ') * 5 for x in range(5)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}


def print_board(board):
    print('  0 1 2 3 4 5')
    print('  +=========+') 
    for row in range(5):
        board.append(['-'] * 5)
    letter = 0
    for row in range(5):
        print(chr(letter * 65), end=' ')
        for column in range(len(board[letter])):
            print(board[letter][column], end=' ')
        print('| ')
        letter += 1
    print(' +=========+')

def create_ships(board):
    for ship in range(3):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == '@':
          ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] 0 '@'  

def get_location():
    pass

def count_hits():
    pass

create_ships()
turns = 8
while turns > 0:
