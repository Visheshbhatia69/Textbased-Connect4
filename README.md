# Textbased-Connect4
A fully working text-based Connect 4 game built in Python (7×6 grid), supporting two players(human vs human as of now), win/tie detection, input validation, and automatic CSV export of all moves.

# Description
Connect Four is a two-player strategy game played on a 7×6 grid. Players alternate turns dropping their chosen symbols into one of the seven columns. The piece falls to the lowest available position.

A player wins by connecting four tokens:

* Horizontally

* Vertically

* Diagonally (both directions)

If the board fills with no winner, the game ends in a tie.

This project implements the complete game in pure Python using classes for board state, players, move handling, input validation, and win detection.
# Features implemented 

* 7×6 game board
* Clean board display
* Player-defined symbols (single character)
* Valid column checking
* Full column detection
* Automatic piece dropping to lowest position
* Horizontal, vertical, and diagonal win detection
* Tie detection when the board is full
* Move-by-move history stored during the game
* Automatic CSV export of all moves with timestamp
* Fully interactive text-based interface
* No external dependencies (uses only Python standard library)

# Project Structure (as of LAST PUSH)

```
connect4/
├── README.md
└── tbconnect4.py
```


# How to Run 

1. Make sure you have Python 3 installed

2. Open a terminal inside the project folder

3 .Run the game using:

```
python tbconnect4.py
```
You will be asked:

* Player 1 name

* Player 1 symbol (1 character)

* Player 2 name

* Player 2 symbol

* Columns to place tokens (1–7)

Game Data Export

After the game ends (win or tie), a CSV file is automatically generated:
```
tbconnect4_moves_YYYYMMDD_HHMMSS.csv
```
The file includes:

* player	
* symbol	
* row	
* col

typing...

