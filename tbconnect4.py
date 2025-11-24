class player():
    # holds players name and symbol 
    def __init__(self, name, number):
        self.name = name
        self.num = number


class board():
    # Making fixed-size Connect 4 board
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

    # Displays the board in a clean format
    def displayboard(self):
        for r in range(self.row):
            for c in range(self.col):
                print("|" + self.board[r][c], end='')
            print("|")
        print("-" * (self.col * 2))

    # Checking if column is full
    def columnFull(self, col):
        # If the top cell is not empty, column is full
        return self.board[0][col] != ' '

    # Placing token
    def addtoken(self, col, sym):
        # Drops token into lowest available space
        for i in range(self.row - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = str(sym)
                break

    # ========== CHECKING WIN CONDITIONS ========== #

    # Check horizontal, vertical, and diagonal win
    def check_winner(self, symbol):

        #horizontal check
        for r in range(self.row):
            for c in range(self.col - 3):
                if (self.board[r][c] == symbol and
                    self.board[r][c+1] == symbol and
                    self.board[r][c+2] == symbol and
                    self.board[r][c+3] == symbol):
                    return True

        #vertical check
        for r in range(self.row - 3):
            for c in range(self.col):
                if (self.board[r][c] == symbol and
                    self.board[r+1][c] == symbol and
                    self.board[r+2][c] == symbol and
                    self.board[r+3][c] == symbol):
                    return True

         # diagonal check up
        for r in range(3, self.row):
            for c in range(self.col - 3):
                if (self.board[r][c] == symbol and
                    self.board[r-1][c+1] == symbol and
                    self.board[r-2][c+2] == symbol and
                    self.board[r-3][c+3] == symbol):
                    return True 
                        
        #diagonal check down
        for r in range(self.row - 3):
            for c in range(self.col - 3):
                if (self.board[r][c] == symbol and
                    self.board[r+1][c+1] == symbol and
                    self.board[r+2][c+2] == symbol and
                    self.board[r+3][c+3] == symbol):
                    return True

        return False



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


# ========= GAME SETUP ========== #

name = input("Player 1s Name: ")
num = input("Player 1s Symbol: ")

name2 = input("Player 2s Name: ")
num2 = input("Player 2s Symbol: ")

player1 = player(name, num)
player2 = player(name2, num2)

b = board()
b.displayboard()


# ========== MAIN GAME LOOP ========= #

while True:

    # Player 1 movves
    col = get_valid_column(player1.name)

    while b.columnFull(col):
        print("Column is full @ @ ")
        col = get_valid_column(player1.name)

    b.addtoken(col, player1.num)
    b.displayboard()

    # WIN CHECK after every move
    if b.check_winner(player1.num):
        print(f"{player1.name} WINNNNNS;)")
        break

    # Player 2 moves
    col = get_valid_column(player2.name)

    while b.columnFull(col):
        print("Column is full @ @ ")
        col = get_valid_column(player2.name)

    b.addtoken(col, player2.num)
    b.displayboard()

    # WIN CHECK after every moove 
    if b.check_winner(player2.num):
        print(f"{player2.name} WINNNNNS;)")
        break
