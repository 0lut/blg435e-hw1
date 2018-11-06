
from copy import deepcopy as copy
from collections import deque
import sys


def sideeffect(f):
    def wrapper(*args):
        newArgs = [copy(arg) for arg in args]
        res = f(*newArgs)
        return res
    return wrapper


def isValidMove(board, piece, direction):
    x, y = piece

    if board[x][y] != 1:
        return False

    if direction == 'U':
        if y > 1 and board[x][y-1] == 1 and board[x][y-2] == 0:
            return True

    elif direction == 'D':
        if y < 5 and board[x][y+1] == 1 and board[x][y+2] == 0:
            return True

    elif direction == 'R':
        if x < 5 and board[x+1][y] == 1 and board[x+2][y] == 0:
            return True

    elif direction == 'L':
        if x > 1 and board[x-1][y] == 1 and board[x-2][y] == 0:
            return True
    return False


@sideeffect
def move(board, piece, direction):

    x, y = piece
    if direction == 'U':
        board[x][y] = 0
        board[x][y-1] = 0
        board[x][y-2] = 1

    elif direction == 'D':
        board[x][y] = 0
        board[x][y+1] = 0
        board[x][y+2] = 1

    elif direction == 'R':
        board[x][y] = 0
        board[x+1][y] = 0
        board[x+2][y] = 1

    elif direction == 'L':
        board[x][y] = 0
        board[x-1][y] = 0
        board[x-2][y] = 1

    return board


def generateMoves(board):
    pieceMoves = []

    for x in range(7):
        for y in range(7):
            movesForPiece = [move(board, (x, y), direction) for direction in [
                'U', 'D', 'R', 'L'] if isValidMove(board, (x, y), direction)]
            pieceMoves.extend(copy(movesForPiece))
    return pieceMoves


def checkGoal(board):
    if len(generateMoves(board)) == 0:
        return True
    return False


def dfs(board):
    frontier = [*generateMoves(board)]
    while True:
        state = frontier.pop()
        newStates = generateMoves(state)
        if len(newStates) == 0:
            printBoard(state)
            return
        frontier.extend(newStates)

def bfs(board):

    frontier = deque()
    frontier.extend(generateMoves(board))
    while True:
        state = frontier.popleft()
        newStates = generateMoves(state)
        if len(newStates) == 0:
            printBoard(state)
            return
        frontier.extend(newStates)

def printBoard(board):

    for q in board:
        print(' '.join(map(str, q)), sep='\n', end='\n')
    print('-------------')


def main():
    board = [['#', '#', 1, 1, 1, '#', '#'], ['#', '#', 1, 1, 1, '#', '#'], *[[1 for i in range(7)] for _ in range(3)], ['#', '#', 1, 1, 1, '#', '#'], ['#', '#', 1, 1, 1, '#', '#'], ]
    board[3][3] = 0
    bfs(board)


if __name__ == '__main__':
    main()
