# migrated from python 2.7
from itertools import *
from functools import reduce

def can_pass(matrix, first, second):
    all_cells = {(row,col) for col in range(len(matrix[0])) for row in range(len(matrix))}
    target_value = matrix[first[0]][first[1]]
    bricks = {(i,j) for (i,j) in all_cells if matrix[i][j]==target_value}
    
    nearby = lambda x, y: {(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)}    

    extend=lambda s: reduce(set.union, list(starmap(nearby, s))) & bricks
    path = {first}

    while extend(path).difference(path):
        path |= extend(path)

    return second in path