# migrated from python 2.7
import math

def checkio(a, b, c):
    if not (a+b>c and a+c>b and b+c>a): return [0,0,0]    
    return sorted([int(round(z, 0)) for z in list(map(math.degrees, list(map(math.acos, [(1.0*(b*b+c*c-a*a)/(2*b*c)),(1.0*(a*a+c*c-b*b)/(2*a*c)),(1.0*(b*b+a*a-c*c)/(2*b*a))]))))])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"