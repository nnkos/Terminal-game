# minesweeper game
import random

# difficulty, board size

def setting(difficulty):
    if difficulty == 'E':
        size = (8, 8)
        mines = 10
    elif difficulty == 'M':
        size = (16, 16)
        mines = 40
    elif difficulty == 'H':
        size = (30, 16)
        mines = 99
    return size, mines

# base board

size, mines = setting('E')

board_ui = [['_'] * size[1] for _ in range(size[0])]

# mines

board_backend = [['_'] * size[1] for _ in range(size[0])]

mines_location_list = []

for _ in range(mines):
    mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[0] - 1))
    while mines_location in mines_location_list:
        mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[0] - 1))
    board_backend[mines_location[1]][mines_location[0]] = 'X'
    mines_location_list.append(mines_location)
    

    
        