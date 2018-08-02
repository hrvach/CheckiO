# migrated from python 2.7
from operator import mul
from functools import reduce

def checkio(attempts):  
    if len(attempts) < 4:
        return (1+len(attempts)*2, 50)

    pairs = [(j,i) for i,j in attempts[1:]]
    
    r = reduce(mul, zip(*pairs)[0], 1)
    res = sum((r/a)*b*pow(r/a, a-2, a) for a,b in pairs) % r

    return (2, res)