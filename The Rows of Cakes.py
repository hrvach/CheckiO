from itertools import combinations
from fractions import Fraction

def checkio(cakes):
    lines, verticals = set(), set()
    
    for (x1,y1),(x2,y2),(x3,y3) in combinations(cakes, 3):        
        if x1==x2==x3:
            verticals.add(x1)
            
        elif [x1,x2,x3].count(0)<2 and x1!=x2:
            k = Fraction(y2-y1, x2-x1)
            l = -k*x1+y1
            if y3==k*x3+l:
                lines.add((k,l))
            
    return len(lines) + len(verticals)