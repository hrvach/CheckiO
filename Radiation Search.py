# migrated from python 2.7
from itertools import *
from functools import reduce

def checkio(matrix):
    width, height = len(matrix[0]), len(matrix)

    elements = {key: 0 for key in set(sum(matrix, []))}
    all_cells = {(row,col) for col in range(width) for row in range(height)}

    member = lambda who, what: any([who in x for x in what])
    
    offsets = [(-1,0), (1,0), (0,-1), (0, 1)]
    nearby = lambda x, y: {(x+a, y+b) for a,b in offsets if \
               (x+a, y+b) in all_cells and matrix[x+a][y+b] == matrix[x][y]}
    
    grow=lambda s: reduce(set.union, list(starmap(nearby, s)))
    partitions = []

    for cell in all_cells:
        if member(cell, partitions): pass
        area = [set(), {cell}]
        for size in takewhile(lambda size: grow(area[-1]) - area[-2], count()):
            area.append(grow(area[-1]) - area[-2])

        partitions.append(reduce(set.union, area))
                   
    largest = max(partitions, key=len)
    length = len(largest)
    
    x,y = largest.pop()
    value = matrix[x][y]

    return [length, value]