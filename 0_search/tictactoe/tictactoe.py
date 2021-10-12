"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    if board == initial_state():
        return X

    xcounter = 0
    ocounter = 0
    for row in board:
        xcounter += row.count(X)
        ocounter += row.count(O)

    if xcounter == ocounter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.append((i, j))
    
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nboard = copy.deepcopy(board)
    try:
        if nboard[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            nboard[action[0]][action[1]] = player(nboard)
            return nboard
    except IndexError:
        print('Spot already occupied')
        print(action)
        return nboard
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]
    for i in range(len(players)):
        #curr = players[i]
        #print(board[0][1], board[1][1], board[2][2], curr)

        # Diagonal check
        if board[0][0] == players[i] and board[1][1] == players[i] and board[2][2] == players[i]:
            return players[i]

        if board[0][2] == players[i] and board[1][1] == players[i] and board[2][0] == players[i]:
            return players[i]

        # Check horizontal
        rec = []
        for j in range(3):
            for k  in range(3):
                rec.append(board[j][k])
            #print(rec)
            if rec[0] == players[i] and rec[1] == players[i] and rec[2] == players[i]:
                return players[i]
            else:
                rec = []

        # check vertical
        rec2 = []
        for m in range(3):
            for n in range(3):
                rec2.append(board[n][m])
            #print(rec2)
            if rec2[0] == players[i] and rec2[1] == players[i] and rec2[2] == players[i]:
                return players[i]
            else:
                rec2 = []

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True

    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def opposite(player):
    if player == X:
        return O
    elif player == O:
        return X

def Max_value(s):
    if terminal(s):
        return utility(s), None
    v = float(-math.inf)
    for action in actions(s):
        #v = max(v, Min_value(result(s, action)))
        u, act = Min_value(result(s, action))
        if u > v:
            v = u
            move = action
    return v, move

def Min_value(s):
    if terminal(s):
        return utility(s), None
    v = float(math.inf)
    for action in actions(s):
        #v = max(v, Max_value(result(s, action)))
        u, act = Max_value(result(s, action))
        if u < v:
            v = u
            move = action
    return v, move

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr = player(board)
    poss_actions = actions(board)
    opp = opposite(curr)

    if board == initial_state():
        return random.choice(poss_actions)
    if curr == X:
        value, move = Max_value(board)
        return move
    else:
        value, move = Min_value(board)
        return move