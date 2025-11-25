import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# ===================== CLASSES =================== #

class player(): #holds players name and symbol
    def __init__(self, name, number):
        self.name = name
        self.num = number

class board(): #Making fixed-size Connect 4 board
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
        print("\nBoard:")
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
    def winner(self, symbol):
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

# ===================== HELPER FUNCTIONS =====================

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

# ================== GUI CLASS (Tkinter) ==================== #

class GUI:
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.current = 0
        self.moves = []

        # Tkinter window
        self.root = tk.Tk()
        self.root.title("Connect 4 GUI")
        self.buttons = []
        self.cells = []

        # Frame for buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        for c in range(self.board.col):
            btn = tk.Button(btn_frame, text=str(c+1), width=8, command=lambda col=c: self.play(col))
            btn.grid(row=0, column=c)
            self.buttons.append(btn)

        # Frame for board cells
        board_frame = tk.Frame(self.root)
        board_frame.pack()

        for r in range(self.board.row):
            row_cells = []
            for c in range(self.board.col):
                lbl = tk.Label(board_frame, text=' ', width=8, height=4, relief='ridge', bg='white', font=('Arial',16))
                lbl.grid(row=r, column=c)
                row_cells.append(lbl)
            self.cells.append(row_cells)

        self.status = tk.Label(self.root, text=f"{self.players[self.current].name} ({self.players[self.current].num}) starts!", font=('Arial',12))
        self.status.pack()

        self.root.mainloop()

    def Board(self):
        for r in range(self.board.row):
            for c in range(self.board.col):
                cell = self.board.board[r][c]
                color = 'white'
                if cell == self.players[0].num:
                    color = 'red'
                elif cell == self.players[1].num:
                    color = 'yellow'
                self.cells[r][c].config(bg=color)

    def play(self, col):
        if self.board.columnFull(col):
            self.status.config(text=f"Column {col+1} is full {self.players[self.current].name}, choose another column.")
            return
        row = self.board.addtoken(col, self.players[self.current].num)
        self.moves.append({
            'player': self.players[self.current].name,
            'symbol': self.players[self.current].num,
            'row': row,
            'col': col
        })
        self.Board()

        # Check for winner
        if self.board.winner(self.players[self.current].num):
            self.status.config(text=f"{self.players[self.current].name} WINNNNNS ;) ")
            self.export_moves()
            self.disable_buttons()
            messagebox.showinfo("Game Over", f"{self.players[self.current].name} WINNNNNS ;) ")
            return

        # Check for tie
        if self.board.is_full():
            self.status.config(text="It's a TIE, focus and play bud :)")
            self.export_moves()
            self.disable_buttons()
            messagebox.showinfo("Game Over", "It's a TIE, focus and play bud :)")
            return

        # Switch player
        self.current = 1 - self.current
        self.status.config(text=f"{self.players[self.current].name} ({self.players[self.current].num})'s turn")

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state='disabled')

    def export_moves(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tbconnect4_gui_moves_{timestamp}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['player','symbol','row','col'])
            writer.writeheader()
            for move in self.moves:
                writer.writerow(move)
        print(f"Moves saved to {filename}")

# ===================== GAME SETUP =====================

name = input("Player 1's Name: ")
num = get_valid_symbol(name)
name2 = input("Player 2's Name: ")
num2 = get_valid_symbol(name2)

player1 = player(name, num)
player2 = player(name2, num2)
b = board()
moves = []

# ===================== CHOOSE MODE =====================

while True:
    mode = input("Choose mode: type 'text' for text mode or 'gui' for GUI: ").strip().lower()
    if mode in ['text', 'gui']:
        break
    print("Invalid choice... Please type exactly 'text' or 'gui'.")

if mode == 'gui':
    gui = GUI(b, player1, player2)
else:
    b.displayboard() # display initial board for text mode

# ========= MAIN GAME LOOP (TEXT MODE) =========

while True:
    # Player 1 moves
    col = get_valid_column(player1.name)
    while b.columnFull(col):
        print("Column is full @ @")
        col = get_valid_column(player1.name)
    row = b.addtoken(col, player1.num)
    b.displayboard()
    moves.append({'player': player1.name, 'symbol': player1.num, 'row': row, 'col': col})
    if b.winner(player1.num):
        print(f"{player1.name} WINNNNNS ;) ")
        winner = player1.name
        break
    if b.is_full():
        print("It's a TIE, focus and play bud :)")
        winner = "Tie"
        break

    # Player 2 moves
    col = get_valid_column(player2.name)
    while b.columnFull(col):
        print("Column is full @ @")
        col = get_valid_column(player2.name)
    row = b.addtoken(col, player2.num)
    b.displayboard()
    moves.append({'player': player2.name, 'symbol': player2.num, 'row': row, 'col': col})
    if b.winner(player2.num):
        print(f"{player2.name} WINNNNNS :) ")
        winner = player2.name
        break
    if b.is_full():
        print("It's a TIE, focus and play bud :)")
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
