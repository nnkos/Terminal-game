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

size, mines = setting('M')

board_ui = [['_'] * size[1] for _ in range(size[0])]

# mines

board_backend = [['_'] * size[1] for _ in range(size[0])]

mines_location_list = []

for _ in range(mines):
    mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
    while mines_location in mines_location_list:
        mines_location = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
    board_backend[mines_location[0]][mines_location[1]] = 'X'
    mines_location_list.append(mines_location)
    
# rest of the board backend

for i in range(size[0]):
    for j in range(size[1]):
        if board_backend[i][j] != 'X':
            mine_counter = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < size[0] and 0 <= y < size[1] and board_backend[x][y] == 'X':
                        mine_counter += 1
            board_backend[i][j] = str(mine_counter)



# borad interaction 

move = list(map(int(input('Enter move here').split(','))))
choice_cell = [move[1] - 1, move[0] - 1]

list_to_reveal_tiles = []
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        cell = [choice_cell[0] + i, choice_cell[1] + j]
        if 0 <= cell[0] < size[0] and 0 <= cell[1] < size[1]:
            list_to_reveal_tiles.append(cell)
            
        