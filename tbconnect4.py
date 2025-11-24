import csv
from datetime import datetime

class player():
    #holds players name and symbol 
    def __init__(self, name, number):
        self.name = name
        self.num = number


class board():
    #Making fixed-size Connect 4 board
    def __init__(self):
        self.col = 7
        self.row = 6
        self.board = []

        # Creates an empty grid
        for r in range(self.row):
            blankrow = []
            for c in range(self.col):
                blankrow.append(' ')
            self.board.append(blankrow)

    #Displays the board in a clean format
    def displayboard(self):
        for r in range(self.row):
            for c in range(self.col):
                print("|" + self.board[r][c], end='')
            print("|")
        print("-" * (self.col * 2))

    #Checking if column is full
    def columnFull(self, col):
        return self.board[0][col] != ' '

    #Placing item/symbol
    def addtoken(self, col, sym):
        for i in range(self.row - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = str(sym)
                return i

    #Check for horizontal, vertical, and diagonal win
    def check_winner(self, symbol):

        #horizontal check
        for r in range(self.row):
            for c in range(self.col - 3):
                if all(self.board[r][c+i] == symbol for i in range(4)):
                    return True

        #vertical check
        for r in range(self.row - 3):
            for c in range(self.col):
                if all(self.board[r+i][c] == symbol for i in range(4)):
                    return True

        #diagonal up
        for r in range(3, self.row):
            for c in range(self.col - 3):
                if all(self.board[r-i][c+i] == symbol for i in range(4)):
                    return True

        #diagonal down
        for r in range(self.row - 3):
            for c in range(self.col - 3):
                if all(self.board[r+i][c+i] == symbol for i in range(4)):
                    return True

        return False

    #Check if board is full (tie)
    def is_full(self):
        return all(self.board[0][c] != ' ' for c in range(self.col))


def get_valid_column(player_name):
    while True:
        try:
            col = int(input(f"{player_name}, choose column (1-7): ")) - 1
            if col < 0 or col > 6:
                print("Column out of range.... Choose 1–7.")
                continue
            return col
        except ValueError:
            print("Invalid input.... Enter a number between 1–7.")


def get_valid_symbol(player_name):
    while True:
        sym = input(f"{player_name}, choose a single-character symbol: ")
        if len(sym) != 1:
            print("Symbol must be exactly 1 character. Try again.")
        else:
            return sym


# ========= GAME SETUP ========== #

name = input("Player 1's Name: ")
num = get_valid_symbol(name)

name2 = input("Player 2's Name: ")
num2 = get_valid_symbol(name2)

player1 = player(name, num)
player2 = player(name2, num2)

b = board()
b.displayboard()

# store moves
moves = []

# ========= MAIN GAME LOOP ========= #

while True:

    # Player 1 moves
    col = get_valid_column(player1.name)
    while b.columnFull(col):
        print("Column is full @ @ ")
        col = get_valid_column(player1.name)

    row = b.addtoken(col, player1.num)
    b.displayboard()
    moves.append({'player': player1.name, 'symbol': player1.num, 'row': row, 'col': col})

    if b.check_winner(player1.num):
        print(f"{player1.name} WINNNNNS;)")
        winner = player1.name
        break

    if b.is_full():
        print("The board is full! It's a TIE!")
        winner = "Tie"
        break

    # Player 2 moves
    col = get_valid_column(player2.name)
    while b.columnFull(col):
        print("Column is full @ @ ")
        col = get_valid_column(player2.name)

    row = b.addtoken(col, player2.num)
    b.displayboard()
    moves.append({'player': player2.name, 'symbol': player2.num, 'row': row, 'col': col})

    if b.check_winner(player2.num):
        print(f"{player2.name} WINNNNNS;)")
        winner = player2.name
        break

    if b.is_full():
        print("The board is full! It's a TIE!")
        winner = "Tie"
        break

# export moves to csv
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"tbconnect4_moves_{timestamp}.csv"

with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['player', 'symbol', 'row', 'col'])
    writer.writeheader()
    for move in moves:
        writer.writerow(move)

print(f"Game moves saved to {filename}")
