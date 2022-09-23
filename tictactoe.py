class TicTacToe:
    isGameWork = True
    player = 'X'
    bot = 'O'
    def __init__(self, board_size):
        self.board = [['#'] * board_size for _ in range(board_size)]
        self.board_size = board_size

    def minimax(self, board, depth, isMax):
        if self.checkSymbolWin(self.bot):
            return 10 - depth
        elif self.checkSymbolWin(self.player):
            return depth - 10
        elif self.checkDraw():
            return 0

        if (isMax):
            bestScore = -1000
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if (board[row][col] == '#'):
                        board[row][col] = self.bot
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = '#'
                        if (score > bestScore):
                            bestScore = score
            return bestScore
        else:
            bestScore = 1000
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if (board[row][col] == '#'):
                        board[row][col] = self.player
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = '#'
                        if (score < bestScore):
                            bestScore = score
            return bestScore

    def printBoard(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                print(self.board[row][col], end='')
            print()

    def doPlayerMove(self):
        row, col = map(int, input("Enter col and row X:  ").split())
        self.insertSymbol(self.player, row - 1, col - 1)
        self.checkStatusGame()

    def doBotMove(self):
        bestScore = -10000
        bestMove = (None, None)
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (self.board[row][col] == '#'):
                    self.board[row][col] = self.bot
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = '#'
                    if (score > bestScore):
                        bestScore = score
                        bestMove = (row, col)
        self.insertSymbol(self.bot, bestMove[0], bestMove[1])
        self.checkStatusGame()

    def checkDraw(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (self.board[row][col] == '#'):
                    return False
        return True

    def checkSymbolWin(self, symbol):
        # Horizontal win
        for row in range(self.board_size):
            isWin = True
            for col in range(self.board_size):
                if self.board[row][col] != symbol:
                    isWin = False
            if isWin:
                return True

        # Vertical win
        for col in range(self.board_size):
            isWin = True
            for row in range(self.board_size):
                if self.board[row][col] != symbol:
                    isWin = False
            if isWin:
                return True

        # Diagonal win
        isWin = True
        for row in range(self.board_size):
            if self.board[row][row] != symbol:
                isWin = False
        if isWin:
            return True

        isWin = True
        for row in range(self.board_size):
            if self.board[row][self.board_size - row - 1] != symbol:
                isWin = False
        if isWin:
            return True

        return False

    def checkIsFree(self, row, col):
        if self.board[row][col] == '#':
            return True
        else:
            return False

    def checkStatusGame(self):
        if (self.checkDraw()):
            print("Draw!")
            self.isGameWork = False
        if self.checkSymbolWin('X'):
            print("Player wins!")
            self.isGameWork = False
        elif self.checkSymbolWin('O'):
            print("Bot wins!")
            self.isGameWork = False

    def insertSymbol(self, symbol, row, col):
        if self.checkIsFree(row, col):
            self.board[row][col] = symbol
        else:
            print("Wrong input, try again")
            self.insertSymbol(symbol, row, col)

    def start(self):
        while self.isGameWork:
            self.printBoard()
            self.doPlayerMove()
            self.doBotMove()
        self.printBoard()