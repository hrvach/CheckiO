# migrated from python 2.7
from itertools import *

def checkio(a, b):
    candidates = [i for i in list(permutations(b)) if 
                    zip(*i[:3])[::2] == [tuple(j)[::2] for j in i[3:]]]

    for c in candidates:
        d = set(sum(starmap(zip, list(zip(c, a[::2]))+list(zip(c[3:], \
                            zip(*a)[::2]))), []))|{(' ', 0)}
        
        if len(d) == len(set(sum(a, []))):
            f = {v: k for k, v in list(dict(d).items())}
            return [[f[i] for i in row] for row in a]