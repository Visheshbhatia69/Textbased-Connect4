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

    #Checking if Column is full
    def columnFull(self, col):
        #If the top cell is not empty, column is full
        return self.board[0][col] != ' '

    #Place token
    def addtoken(self, col, sym):
        #Drops token into lowest available space
        for i in range(self.row - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = str(sym)
                break


#input function for selecting columns
def get_valid_column(player_name):
    while True:
        try:
            #Get input and convert to index
            col = int(input(f"{player_name}, choose column (1-7): ")) - 1

            #Check number if in range
            if col < 0 or col > 6:
                print("Column out of range! Choose 1–7.")
                continue

            return col

        except ValueError:
            print("Invalid input! Enter a number between 1–7.")


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

    #Player 1 turn
    col = get_valid_column(player1.name)

    #Check if full
    while b.columnFull(col):
        print("Column is full! Choose another one.")
        col = get_valid_column(player1.name)

    b.addtoken(col, player1.num)
    b.displayboard()

    #Player 2 turn
    col = get_valid_column(player2.name)

    while b.columnFull(col):
        print("Column is full! Choose another one.")
        col = get_valid_column(player2.name)

    b.addtoken(col, player2.num)
    b.displayboard()
