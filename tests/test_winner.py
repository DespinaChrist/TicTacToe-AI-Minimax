import pytest
from tictactoe import winner
from tictactoe import O
from tictactoe import X
from tictactoe import EMPTY

def test_horizontal_win():
    boardh = [[X, X, X],
    [O, O, X],
    [O, X, O]]
    assert winner(boardh) == X

def test_vertical_win():
    boardv = [[X, O, X],
    [X, O, X],
    [X, O, O]]
    assert winner(boardv) == X

def test_diagonal_win():
    boardd = [[X, O, X],
    [O, X, O],
    [X, O, X]]
    assert winner(boardd) == X

def test_no_win():
    boardn = [[X, O, X],
    [O, X, O],
    [O, X, O]]
    assert winner(boardn) == None

def test_tie():
    boardt = [[X, O, X],
    [X, O, X],
    [O, X, O]]
    assert winner(boardt) == None