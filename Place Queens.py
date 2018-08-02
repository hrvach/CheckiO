# migrated from python 2.7
from operator import add,sub
from itertools import product

cols, rows = set('abcdefgh'), set('12345678')
whole_board = set(map(''.join,product(cols, rows)))


def cell_under_attack(board_set, cell):
    coord = lambda c: list(map(ord, list(c)))
    diag1, diag2 = sub(*coord(cell)), add(*coord(cell))

    return {fig for fig in board_set if any([sub(*coord(fig))==diag1,
        add(*coord(fig))==diag2, cell[0]==fig[0], cell[1]==fig[1]])}


def traverse(board):    
    candidate_cells = set(cell for cell in whole_board if \
        cell[0] not in zip(*board)[0] and cell[1] not in zip(*board)[1])

    if not candidate_cells and len(board)==8: return board

    for cell in candidate_cells:
        if not cell_under_attack(board, cell):
            result = traverse(board|{cell})
            if result: return result            
    return set()

def place_queens(board):
    if any([cell_under_attack(board-{cell}, cell) for cell in board]):
        return set()
    else:
        return traverse(board)