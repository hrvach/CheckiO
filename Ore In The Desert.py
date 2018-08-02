# migrated from python 2.7
from itertools import *
from math import hypot

def checkio(previous):
    all_cells = set(product(list(range(10)), repeat=2))

    number_of_probes = len(previous)

    if number_of_probes < 1:
        return [4,5]

    distance = lambda x, y: round(hypot(abs(x[0]-y[0]), abs(x[1]-y[1])))
    possible = [{c for c in all_cells if distance(c, (x,y)) == r} for (x,y,r) in previous]
    
    return reduce(set.intersection, possible).pop()