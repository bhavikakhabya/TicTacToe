🎯 Tic-Tac-Toe (Python)

How to Run

1. Make sure Python 3 is installed.

2. Download or clone the project folder.

3. Open terminal in the project directory.

4. Run the game using:


python tic_tac_toe.py


---------

How to Play

The board has 9 positions numbered 1 to 9:


1 | 2 | 3

--+---+--

4 | 5 | 6

--+---+--

7 | 8 | 9

Player X starts the game.

Enter a number (1–9) to place your mark.

If the position is already filled, the game will ask you to choose again.

The game ends when:

A player wins

Or all spaces are filled (draw)


-----------

Example

Player X turn.
Choose a position (1-9): 5

Player O turn.
Choose a position (1-9): 1

Player X wins! 🎉

---

Code Description

board → Stores the 3×3 game board

display_board() → Shows the board

check_win(player) → Detects winning combinations

check_draw() → Checks if the board is full

Main loop → Takes input, updates board, checks win/draw, switches turns
