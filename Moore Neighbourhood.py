# migrated from python 2.7
from itertools import product

def count_neighbours(grid, row, col):
    return sum([grid[row+i][col+j] for (i,j) in list(product(*[list(range(-1,2))]*2)) \
        if {(row+i, col+j)}<{(x,y) for (x,y) in list(product(*list(map(range, \
        (len(grid),len(grid[0]))))))}]) - grid[row][col]