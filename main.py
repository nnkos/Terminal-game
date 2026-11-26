import time
from minesweeper import (
    setting,
    make_board,
    place_mines,
    fill_backend,
    flood_fill,
    check_lose,
    check_win,
    print_board,
    move_action,
    move_stats,
)
 
 
def main():
    size, mines = setting('E')
 
    board_ui = make_board(size)
    board_backend = make_board(size)
 
    mines_location_list = place_mines(board_backend, mines, size)
    fill_backend(board_backend, size)
  
    move_counter = 0
    no_mines_counter = mines
    elapsed_time = 0
    game_status = 1
    game_start_time = time.perf_counter()
 
    while game_status == 1:
        print_board(board_ui)
        print(f'Moves: {move_counter} | Mines left: {no_mines_counter}')
 
        try:
            action, choice_cell = move_action(board_ui)
        except (ValueError, IndexError):
            print('Invalid move, please use the format F,x,y or D,x,y')
            continue
        r, c = choice_cell
 
        if action == 'D':
            if board_ui[r][c] == 'F':
                print('That cell is flagged. Remove the flag first (F,x,y).')
                continue
            if board_ui[r][c] != '_':
                print('That cell is already revealed.')
                continue
            board_ui = flood_fill(board_ui, board_backend, choice_cell, size)
            if board_backend[r][c] == 'X':
                board_ui = check_lose(board_backend, choice_cell, board_ui)
                game_status = 0
 
        move_counter, no_mines_counter, elapsed_time = move_stats(
            board_ui, size, mines, move_counter, game_start_time
        )
 
        if game_status == 1:
            board_ui, game_status = check_win(board_ui, board_backend, size, mines, mines_location_list)
 
    print_board(board_ui)
    print(f'Moves: {move_counter} | Time: {elapsed_time:.1f}s')
 
 
if __name__ == '__main__':
    main()