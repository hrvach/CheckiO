from functools import reduce
from itertools import *

def checkio(land_map):
    board = {(i, j) for j in range(len(land_map[0])) for i in range(len(land_map))}
    land = {(i,j) for i,j in board if land_map[i][j] == 1}

    nearby = lambda x,y: {(x+a, y+b) for a,b in set(product(*[(0,-1,1)]*2))}
    grow=lambda s: reduce(set.union, list(starmap(nearby, s)))

    islands = []
   
    while land:
        area = [set(), set(), {min(land)}]
        while area[-1]-area[-2]:            
            area.append(grow(area[-1]-area[-2]) & land)
            land = land - area[-1]

        area = reduce(set.union, area)
        islands.append(len(area))

    return sorted(islands)