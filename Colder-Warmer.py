# migrated from python 2.7
from itertools import *
from math import hypot

from operator import eq, le, ge

def checkio(moves=[0,0]):
    cells = set(product(list(range(10)), repeat=2))    
    dist = lambda x, y: round(hypot(abs(x[0]-y[0]), abs(x[1]-y[1])))

    if not len(moves)>1:
        x,y,_=moves[0]
        return (max(x/2, (10-x)/2)), max((y/2), (10-y)/2)

    possible = []
    
    for ((x_prev, y_prev, _),(x, y, hint)) in zip(moves, moves[1:]):    
        metric = [eq, le, ge][2**(hint > 0) - (hint == 0)]
        possible.append({c for c in cells if c!=(x,y) and \
                metric(dist(c, (x_prev,y_prev)), dist(c, (x,y)))})

    return reduce(set.intersection, possible).pop()