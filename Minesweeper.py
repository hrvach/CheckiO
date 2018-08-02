from itertools import *
from functools import reduce

def checkio(field):
    board = tuple(product(range(len(field)), repeat=2))
    finder = lambda x: {(i, j) for i,j in board if field[i][j]==x}
   
    unopened, *mines_around, mines = tuple(map(finder, [-1] + list(range(1,10))))
    opened = reduce(set.union, mines_around)

    adjacent = {(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1)}
    neighbors = lambda x,y: {(x+row, y+col) for row, col in adjacent} 

    for x,y in opened:
        around = neighbors(x, y)
        unopened_cells_around = around & unopened
        mines_around = around & mines

        if not unopened_cells_around:
            continue       
        
        if len(unopened_cells_around | mines_around) == field[x][y]:
            mine_x, mine_y = unopened_cells_around.pop()          
            return [True, mine_x, mine_y]

        if field[x][y] == len(mines_around):
            safe_cells = unopened_cells_around - mines_around
            if len(safe_cells):
                not_mine_x, not_mine_y = safe_cells.pop()
                return [False, not_mine_x, not_mine_y]

    return [False, 0, 0]