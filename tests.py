from tictactoe import TicTacToe

def test_init():
    game = TicTacToe(3)
    assert game.board_size == 3
    for row in range(game.board_size):
        for col in range(game.board_size):
            assert game.board[row][col] == '#'

def test_insert():
    game = TicTacToe(3)
    game.insertSymbol('X', 1, 1)
    assert game.board[1][1] == 'X'
    game.insertSymbol('O', 1, 2)
    assert game.board[1][2] == 'O'

def test_horizontal_win():
    game = TicTacToe(3)
    game.insertSymbol('X', 0, 0)
    game.insertSymbol('X', 0, 1)
    game.insertSymbol('X', 0, 2)
    assert game.checkSymbolWin('X')
    assert game.checkSymbolWin('O') == False
    assert game.isGameWork == False

def test_vertical_win():
    game = TicTacToe(3)
    game.insertSymbol('X', 0, 0)
    game.insertSymbol('X', 1, 0)
    game.insertSymbol('X', 2, 0)
    assert game.checkSymbolWin('X')
    assert game.checkSymbolWin('O') == False
    assert game.isGameWork == False

def test_diagonal1_win():
    game = TicTacToe(3)
    game.insertSymbol('X', 0, 0)
    game.insertSymbol('X', 1, 1)
    game.insertSymbol('X', 2, 2)
    assert game.checkSymbolWin('X')
    assert game.checkSymbolWin('O') == False
    assert game.isGameWork == False

def test_diagonal2_win():
    game = TicTacToe(3)
    game.insertSymbol('X', 0, 2)
    game.insertSymbol('X', 1, 1)
    game.insertSymbol('X', 2, 0)
    assert game.checkSymbolWin('X')
    assert game.checkSymbolWin('O') == False
    assert game.isGameWork == False

if __name__ == '__main__':
    test_init()
    test_insert()
    test_horizontal_win()
    test_vertical_win()
    test_diagonal1_win()
    test_diagonal2_win()
