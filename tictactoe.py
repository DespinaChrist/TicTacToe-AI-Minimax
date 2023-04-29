"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = 0
    for row in board:
        for cell in row:
            if cell != EMPTY:
                moves += 1

    if moves % 2 == 0:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valid_actions = actions(board)
    board_copy = copy.deepcopy(board)

    if action not in valid_actions:
        raise RuntimeError
    else:
        board_copy[action[0]][action[1]] = player(board)
    
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    vertical_winner = check_vertically(board)
    if vertical_winner is not None:
        return vertical_winner
    horizontal_winner = check_horizontally(board)
    if horizontal_winner is not None:
        return horizontal_winner    
    diagonal_winner = check_diagonally(board)
    if diagonal_winner is not None:
        return diagonal_winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or is_full(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    curr_winner = winner(board)
    if curr_winner is X:
        return 1
    elif curr_winner is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    moves = {}
    curr_player = player(board)
    possible_actions = actions(board)

    if curr_player == X:
        for action in possible_actions:
            moves[action] = min_value(result(board, action))
        return max(moves, key=moves.get)
    else:
        for action in possible_actions:
            moves[action] = max_value(result(board, action))
        return min(moves, key=moves.get)
    
        

def check_vertically(board):
    for i in range(3):
        items = [item[i] for item in board]
        have_winner, winner = all_equal(items)
        if have_winner:
            return winner
        

def check_horizontally(board):
    for list in board:
        have_winner, winner = all_equal(list)
        if have_winner:
            return winner

def check_diagonally(board):
    diag_prim = [board[i][i] for i in range(len(board))]
    have_winner, winner = all_equal(diag_prim)
    if have_winner:
        return winner
    diag_sec = [board[i][len(board)-i-1] for i in range(len(board))]
    have_winner, winner = all_equal(diag_sec)
    if have_winner:
        return winner

def all_equal(list):
    if all(ele == X for ele in list):
        return (True, X)
    if all(ele == O for ele in list):
        return (True, O)
    return (False, None)

def is_full(board):
    for row in board:
        for item in row:
            if item is EMPTY:
                return False
    return True


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -2
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = 2
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value

    