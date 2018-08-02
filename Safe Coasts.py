# migrated from python 2.7
from itertools import *
from functools import reduce

def finish_map(chart):
    print(chart)
    board = {(i, j) for j in range(len(chart[0])) for i in range(len(chart))}
    
    finder = lambda x: {(i,j) for i,j in board if chart[i][j]==x}
    ships, obstacles, water = list(map(finder, 'DX.'))

    diag = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
    adjacent = set(product(*[(0,-1,1)]*2))-{(0,0)} | diag
    
    nearby = lambda x,y: {(x+a, y+b) for a,b in adjacent}    
    grow=lambda s: reduce(set.union, list(starmap(nearby, s))) if s else set()
    forbidden = grow(obstacles) & board
    adjacent -= diag    

    area = [set(), ships]
    while area[-1]-area[-2]:
        increase = (grow(area[-1]) - area[-2]) & water - forbidden
        area.append(increase)            
    area = reduce(set.union, area)

    chart = list(map(list, chart))
    for row,val in enumerate(chart):
        for col,i in enumerate(val):
            if i != '.': continue
            chart[row][col]=('D' if (row,col) in area else 'S')
    
    return list(map(''.join, chart))