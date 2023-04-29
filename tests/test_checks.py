import pytest
from tictactoe import check_diagonally
from tictactoe import check_horizontally
from tictactoe import check_vertically
from tictactoe import X
from tictactoe import O
from tictactoe import EMPTY

# Check Horizontally
def test_board_1():
    board1 =     [[X, X, X],
                [X, EMPTY, EMPTY],
                [O, EMPTY, EMPTY]]


    assert check_vertically(board1) == None
    assert check_diagonally(board1) == None
    assert check_horizontally(board1) == X

def test_board_2():
    board2 =     [[EMPTY, X, X],
                [X, EMPTY, EMPTY],
                [X, X, X]]


    assert check_vertically(board2) == None
    assert check_diagonally(board2) == None
    assert check_horizontally(board2) == X

def test_board_3():
    board3 =     [[X, EMPTY, EMPTY],
                [O, O, O],
                [O, EMPTY, EMPTY]]


    assert check_vertically(board3) == None
    assert check_diagonally(board3) == None
    assert check_horizontally(board3) == O


#Check Vertically
def test_board_4():
    board4 =     [[X,EMPTY, X],
                [X, EMPTY, EMPTY],
                [X, EMPTY, EMPTY]]


    assert check_vertically(board4) == X
    assert check_diagonally(board4) == None
    assert check_horizontally(board4) == None

def test_board_5():
    board5 = [[O, X, X],
    [O, X, O],
    [O, X, O]]
    assert check_horizontally(board5) == None
    assert check_vertically(board5) == O
    assert check_diagonally(board5) == None

def test_board_6():
    board6 = [[X, O, X],
    [O, O, X],
    [X, X, O]]
    assert check_horizontally(board6) == None
    assert check_vertically(board6) == None
    assert check_diagonally(board6) == None

# Check Diagonally
def test_board_7():
    board7 = [[X, O, O],
    [O, X, O],
    [O, X, X]]
    assert check_horizontally(board7) == None
    assert check_vertically(board7) == None
    assert check_diagonally(board7) == X

def test_board_8():
    board8 = [[O, X, O],
    [X, O, X],
    [O, X, O]]
    assert check_horizontally(board8) == None
    assert check_vertically(board8) == None
    assert check_diagonally(board8) == O