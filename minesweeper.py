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

def make_board(size):
    return [['_'] * size[1] for _ in range(size[0])]

# mines

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
                
#lose condition

def check_lose(board_backend, choice_cell, board_ui):
    if board_backend[choice_cell[0]][choice_cell[1]] == 'X':
        print('Game over, you lose')
        board_ui = board_backend
        return board_ui
    
# win condition
 
def check_win(board_ui, board_backend, size, mines, mines_location_list):
    game_status = 1

    # check win condition
    unrevealed_cells = 0
    for r in range(size[0]):
        for c in range(size[1]):
            if board_ui[r][c] == '_' or board_ui[r][c] == 'F':
                unrevealed_cells += 1

    if unrevealed_cells == mines: 
        print('Congratulations, you won!')
        # Reveal all mines as flags
        board_ui = board_backend
        for r, c in mines_location_list:
            board_ui[r][c] = 'F'
        game_status = 0

    return board_ui, game_status

#flood fill reveal 

def flood_fill(board_ui, board_backend, choice_cell, size):

    if board_backend[choice_cell[0]][choice_cell[1]] == 'X':
        return board_ui
    
    to_check = [choice_cell]
    while to_check:
        r, c = to_check.pop()
        if board_ui[r][c] != '_':
            continue
        board_ui[r][c] = board_backend[r][c]

        if board_backend[r][c] == '0':
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    x, y = r + i, c + j
                    if 0 <= x < size[0] and 0 <= y < size[1]:
                        to_check.append([x, y])
 
    return board_ui

# move action

def move_action(board_ui):
    print('Enter move here in the following format : F,x,y or D,x,y (where F is a flag or D is to dig, with x and y being the coordinates)')
    move = input().upper()
    print(move)
 
    parts = move.split(',')
    action = parts[0]
    choice_cell = [int(parts[2]) - 1, int(parts[1]) - 1]
 
    if action == 'F' and board_ui[choice_cell[0]][choice_cell[1]] == '_':
        board_ui[choice_cell[0]][choice_cell[1]] = 'F'
    elif action == 'F' and board_ui[choice_cell[0]][choice_cell[1]] == 'F':
        board_ui[choice_cell[0]][choice_cell[1]] = '_'
    elif action == 'F':
        print('You cannot flag a revealed cell.')
        raise ValueError('Revealed cell')
    elif action == 'D':
        pass
 
    return action, choice_cell

#show board
 
def print_board(board_ui):
    rows, cols = len(board_ui), len(board_ui[0])
    width = len(str(max(rows, cols)))          # width of the biggest axis number

    header = ' ' * (width + 3) + ' '.join(f'{c:>{width}}' for c in range(1, cols + 1))
    divider = ' ' * (width + 1) + '+' + '-' * (len(header) - width - 1)

    print(header)
    print(divider)
    for r, row in enumerate(board_ui, 1):
        print(f'{r:>{width}} | ' + ' '.join(f'{cell:>{width}}' for cell in row))
    print()

#stats 

def move_stats(board_ui, size, mines, move_counter, game_start_time):
    end_time = time.perf_counter()
    elapsed_time = end_time - game_start_time

    move_counter += 1
 
    no_mines_counter = 0
    for i in range(size[0]):
        for j in range(size[1]):
            if board_ui[i][j] == 'F':
                no_mines_counter += 1
    no_mines_counter = mines - no_mines_counter
 
    return move_counter, no_mines_counter, elapsed_time
