class player():
    #Holds players name and symbol 
    def __init__(self, name, number):
        self.name = name
        self.num = number


class board():
    #Making fixed-size Connect 4 board
    def __init__(self):
        self.col = 7
        self.row = 6
        self.board = []

        #Creates an empty grid
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

    #Places a token in a column
    def addtoken(self, col, sym):
        # Drops token into lowest available space
        for i in range(self.row - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = str(sym)
                break


# ========= GAME SETUP ========== #

name = input("Player 1 Name: ")
num = input("Player 1 Symbol: ")

name2 = input("Player 2 Name: ")
num2 = input("Player 2 Symbol: ")

player1 = player(name, num)
player2 = player(name2, num2)

b = board()
b.displayboard()


# ========== MAIN GAME LOOP ========= #

while True:
    # Player 1 movves
    col = int(input(f"{player1.name}, choose column (1-7): ")) - 1
    b.addtoken(col, player1.num)
    b.displayboard()

    # Player 2 moves
    col = int(input(f"{player2.name}, choose column (1-7): ")) - 1
    b.addtoken(col, player2.num)
    b.displayboard()
