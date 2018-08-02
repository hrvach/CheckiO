# migrated from python 2.7
from itertools import *
from functools import reduce

def knights(first, second, moves=0):
    cells = {product(list(range(8)), repeat=2)}
    
    directions = [[(-1, 1), (-2, 2)], [(-2, 2), (-1, 1)]]
    offsets = set(reduce(chain, list(starmap(product, directions))))

    remove_impossible = lambda s: {(x,y) for (x,y) in s if 8>x>=0 and 8>y>=0}
    nearby = lambda x, y: {(x,y)} | remove_impossible({(x+dx,y+dy) for dx,dy in offsets})
    
    extend=lambda s: reduce(set.union, list(starmap(nearby, s))).difference(s)
    path = {first}

    for moves in takewhile(lambda moves: second not in path, count(1)):
        path |= extend(path)
        
    return moves

def checkio(cells):
    convert = lambda x: (ord(x[0])-97, int(x[1])-1)
    return knights(*list(map(convert, cells.split('-'))))