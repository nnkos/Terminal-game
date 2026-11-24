from minesweeper import (
    setting,
    make_board,
    place_mines,
    fill_backend,
    get_move,
    flood_fill,
    check_lose,
    check_win,
    print_board,
)
 
 
def main():
    size, mines = setting('M')
 
    board_ui = make_board(size)
    board_backend = make_board(size)
 
    mines_location_list = place_mines(board_backend, size, mines)
    fill_backend(board_backend, size)
 
    choice_cell = get_move()
 
    board_ui = flood_fill(board_ui, board_backend, choice_cell, size)
    board_ui = check_lose(board_ui, board_backend, choice_cell)
    board_ui, game_status = check_win(board_ui, board_backend, size, mines, mines_location_list)
 
    print_board(board_ui)
 
 
if __name__ == '__main__':
    main()