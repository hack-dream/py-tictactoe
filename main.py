from tictactoe import TicTacToe

if __name__ == '__main__':
    board_size = int(input('Input board size: '))
    game = TicTacToe(board_size)
    game.start()
