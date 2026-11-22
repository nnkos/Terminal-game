# minesweeper game
import random
import math
import time

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

size, mines = setting('M')

def make_board(size):
    return [['_'] * size[1] for _ in range(size[0])]

# mines

board_backend = [['_'] * size[1] for _ in range(size[0])]

def place_mines(board_backend, mines, size):
    mines_location_list = []

    for _ in range(mines):
        mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        while mines_location in mines_location_list:
            mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        board_backend[mines_location[0]][mines_location[1]] = 'X'
        mines_location_list.append(mines_location)
    
    return mines_location_list
    
# rest of the board backend

def fill_backend(board_backend, size):

    for i in range(size[0]):
        for j in range(size[1]):
            if board_backend[i][j] != 'X':
                mine_counter = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < size[0] and 0 <= y < size[1] and board_backend[x][y] == 'X':
                            mine_counter += 1
                board_backend[i][j] = str(mine_counter)



# board interaction 

def get_move():
    move = list(map(int(input('Enter move here').split(','))))
    choice_cell = [move[1] - 1, move[0] - 1]
    return choice_cell

def get_tiles_to_reveal(choice_cell, size):
    list_to_reveal_tiles = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            cell = [choice_cell[0] + i, choice_cell[1] + j]
            if 0 <= cell[0] < size[0] and 0 <= cell[1] < size[1]:
                list_to_reveal_tiles.append(cell)
    return list_to_reveal_tiles


# Randomly select a number of cells to reveal 

def get_reveal_count(list_to_reveal_tiles):

    lower = max(3, math.ceil(0.33 * len(list_to_reveal_tiles)))
    upper = math.ceil(0.67 * len(list_to_reveal_tiles))
    if lower > upper:
        no_revealed_tiles = lower
    else: 
        no_revealed_tiles = random.randint(lower, upper)
    return no_revealed_tiles

# revealing the chosen cell

def reveal_chosen_cell(board_ui, board_backend, no_revealed_tiles, list_to_reveal_tiles, choice_cell):

    board_ui[choice_cell[0]][choice_cell[1]] = board_backend[choice_cell[0]][choice_cell[1]]
    no_revealed_tiles -= 1
    list_to_reveal_tiles.remove(choice_cell)
    return no_revealed_tiles
    

#lose condition
def check_lose(board_backend, choice_cell, board_ui):
    if board_backend[choice_cell[0]][choice_cell[1]] == 'X':
        print('Game over, you lose')
        board_ui = board_backend
    
