# minesweeper game
import random

# difficulty, board size

def minesweeper(difficulty):
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

size, mines = minesweeper('E')

board_ui = [['_'] * size[1] for _ in range(size[0])]

print(board_ui)