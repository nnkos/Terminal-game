# Terminal-game
Minesweeper

How to run
1. Put main.py and minesweeper.py in the same folder.
2. Open a terminal in that folder (in VS Code, right-click main.py and choose Open in Integrated Terminal).

Run: python main.py

3. Enter moves in the format F,x,y to flag or unflag a cell, or D,x,y to dig. x is the column and y is the row, both counted from 1 using the axis numbers on the board. For example, D,5,3 digs column 5, row 3.

4. The difficulty is set in main() with setting('M'). Change 'M' to 'E' for Easy (8x8, 10 mines) or 'H' for Hard (30x16, 99 mines).

Features
1. Three difficulty levels: Easy, Medium and Hard
2. Random mine placement, with each cell showing how many mines touch it
3. Flood-fill reveal, so digging an empty cell opens the whole empty area around it
4. Flagging and unflagging of suspected mines
5. A board with column and row numbers
6. A move counter and a mines-left counter, which is the total mines minus the flags placed
7. An elapsed-time display
8. Input checks that reject bad input
9. Win and lose detection, with the full board shown when the game ends

Main logic: At the start, main() builds both boards, places the mines, and fills in the numbers. It then loops until the game ends. Each turn it reads a move, and a flag move inputs F on the visible board. A dig move runs the flood fill, which reveals the chosen cell and keeps spreading outward from any cell with a count of 0. If the dug cell is a mine, the player loses. Otherwise the counters update, and the player wins once the only cells left hidden or flagged are exactly as many as there are mines.